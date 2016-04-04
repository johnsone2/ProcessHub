import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse, QueryDict, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from common import parse_request_body
from services.jira_client_service import JiraClientService
from standup.forms.standup_task_form import StandupTaskForm, StandupTaskWorkForm
from services.standup_task_service import StandupTaskService


class StandupTaskView(LoginRequiredMixin, View):

    def __init__(self, **kwargs):
        super(StandupTaskView, self).__init__(**kwargs)
        self.standup_task_service = StandupTaskService()

    def _get_context(self, standup_task_form, standup_task_work_form, *args, **kwargs):
        jira_service = JiraClientService()

        jira_issues = jira_service.get_issues_in_project("DER")
        context = {
            'standup_task_form': standup_task_form,
            'standup_task_work_form': standup_task_work_form,
            'jira_issues': jira_issues
        }
        return context

    def get(self, request):
        context = self._get_context(StandupTaskForm(), StandupTaskWorkForm(), blah="blah", foo="bar")
        return render(request, 'standup/index.html', context)

    def post(self, request):
        request_body = parse_request_body(request)

        standup_task_form = StandupTaskForm(request_body)
        standup_task_work_form = StandupTaskWorkForm(request_body)
        try:
            create_result = self.standup_task_service.create_standup_task_with_work(
                standup_task_form, standup_task_work_form, request.user
            )
            location_uri = request.build_absolute_uri() + str(create_result)
            if request.is_ajax():
                response = HttpResponse(status=201)
                response["Location"] = location_uri

                return response

            return HttpResponseRedirect('/standup/')

        except ValueError as e:
            if request.is_ajax():
                errors_dict = e.args[0]
                return HttpResponse(status=400, content_type="application/json", content=json.dumps(errors_dict))

            context = self._get_context(standup_task_form, standup_task_work_form)
            return render(request, 'standup/index.html', context)
        except Exception as e:
            if request.is_ajax():
                return HttpResponse(status=500, content=e.args[0])

            context = self._get_context(standup_task_form, standup_task_work_form)
            return render(request, 'standup/index.html', context)


