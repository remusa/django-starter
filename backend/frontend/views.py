from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.middleware.csrf import get_token


def index(request):
    return render(request, "frontend/index.html")


def csrf(request):
    return JsonResponse({"csrfToken": get_token(request)})


def ping(request):
    return JsonResponse({"result": "OK"})
