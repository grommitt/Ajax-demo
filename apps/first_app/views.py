from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from django.core import serializers
import json
def index(request):
    return render(request, 'first_app/index.html')
def all_json(request):
    users = User.objects.all()
    users_json = serializers.serialize("json", users)
    return HttpResponse(users_json, content_type='application/json')
def all_html(request):
    users = User.objects.all()
    return render(request, 'first_app/all.html', { "users": users })