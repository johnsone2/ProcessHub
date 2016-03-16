import json

from django.http import HttpResponse, JsonResponse, QueryDict
from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from common.binding_model_converter import BindingModelConverter
from services.jira_client_service import JiraClientService
from services.standup_task_service import StandupTaskService


def parse_request_body(self, request):
    if request.POST:
        request_body = request.POST.dict()
        request_body = self._convert_string_bools_to_bools(request_body)
    else:
        try:
            request_body = json.loads(request.body)
        except BaseException as e:
            try:
                request_body = QueryDict(request.body).dict()
                request_body = self._convert_string_bools_to_bools(request_body)
            except BaseException as e:
                request_body = {}

    return request_body


class StandupTaskView(View):

    def __init__(self, **kwargs):
        super(StandupTaskView, self).__init__(**kwargs)
        self.standup_task_service = StandupTaskService()

    def get(self, request):
        pass

    def put(self, request):
        client = JiraClientService()
        response = client.log_time_on_issue("DER-54", .5)
        return JsonResponse(response)

    def post(self, request):
        request_body = parse_request_body(request)

        