from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from common import parse_request_body


class AuthenticationView(View):
    def post(self, request):
        request_body = parse_request_body(request)
        user = authenticate(username=request_body.get('username'), password=request_body.get('password'))
        if user is None or not user.is_active:
            return HttpResponse(status=401)
        login(request, user)
        return HttpResponse()