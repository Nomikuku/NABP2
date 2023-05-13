from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "planner/index.html")

def about(request):
    return render(request, "planner/about.html")

def tasks(request):
    return render(request, "planner/tasks.html")

def add(request):
    return render(request, "planner/add.html")

def block(request):
    return render(request, "planner/block.html")
