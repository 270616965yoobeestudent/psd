from django.http import HttpResponse
from django.shortcuts import render

def welcome(request, name):
    context = {"name": name}
    return render(request, "example/welcome.html", context)