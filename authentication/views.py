from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import View


def hello_world(request, *args, **kwargs):
    return HttpResponse("Hello World")

def redirect_to_standup(request):
    return redirect('/standup/')