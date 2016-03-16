import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse, QueryDict
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

    def get(self, request):
        jira_service = JiraClientService()

        jira_issues = jira_service.get_issues_in_project("DER")
        context = {
            'standup_task_form': StandupTaskForm(),
            'standup_task_work_form': StandupTaskWorkForm(),
            'jira_issues': jira_issues
        }
        return render(request, 'standup/index.html', context)

    def post(self, request):
        try:

            request_body = parse_request_body(request)

            standup_task_form = StandupTaskForm(request_body)
            standup_task_work_form = StandupTaskWorkForm(request_body)

            create_result = self.standup_task_service.create_standup_task_with_work(
                standup_task_form, standup_task_work_form, request.user
            )
            location_uri = request.build_absolute_uri() + str(create_result)
            response = HttpResponse(status=201)
            response["Location"] = location_uri

            return response
        except ValueError as e:
            return HttpResponse(status=400, content_type="application/json", content=json.dumps(e.args[0]))
        except Exception as e:
            return HttpResponse(status=500, content=e.args[0])


