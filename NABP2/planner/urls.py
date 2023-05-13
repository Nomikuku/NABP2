from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("tasks", views.tasks, name="tasks"),
    path("add", views.add, name="add"),
    path("block", views.block, name="block")
]