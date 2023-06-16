from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy

from django.views.generic import (ListView, CreateView, UpdateView, DeleteView,)
from .models import ToDoItem, ToDoList
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
import requests

TELEGRAM_BOT_TOKEN = "992737156:AAHJH8m9uf8RmjWp3Sv8hkFAtN6buoMiS1s"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

chat_id = "1252733785"
chat_group_id = "-1001711230898"


@method_decorator(login_required, name="dispatch")
class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"
    
@method_decorator(login_required, name="dispatch")
class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context

@method_decorator(login_required, name="dispatch")
class ListCreate(CreateView):
    model = ToDoList
    fields = ["title"]

    def get_context_data(self):
        context = super().get_context_data()
        context["title"] = "Add a new list"
        return context

@method_decorator(login_required, name="dispatch")
class ItemCreate(CreateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_initial(self):
        initial_data = super().get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super().get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])


        link = "http://ematevez1.pythonanywhere.com/todo/"
        payload = str(todo_list) + ", asigno un nueva tarea: " + "\n" + str(self.object) + "\n" + link
        
        params = {"chat_id": chat_id, "parse_mode": "Markdown", "text":payload}
        requests.get(TELEGRAM_API_URL, params=params)
        params1 = {"chat_id": chat_group_id , "parse_mode": "Markdown", "text":payload}
        requests.get(TELEGRAM_API_URL, params=params1)
        
        return reverse("list", args=[self.object.todo_list_id])

@method_decorator(login_required, name="dispatch")
class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]
    

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

@method_decorator(login_required, name="dispatch")
class ListDelete(DeleteView):
    model = ToDoList
    # You have to use reverse_lazy() instead of reverse(),
    # as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("dashboard")

@method_decorator(login_required, name="dispatch")
class ItemDelete(DeleteView):
    model = ToDoItem

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context
    
@login_required
def vista(request):
    if request.user.profile.job == "2K" or request.user.profile.job == "COMANDANTE":
        contexts = ToDoList.objects.all()
    else:    
        contexts = ToDoList.get(title=requests.user.profile.job)
    return render(request, "todo_app/index.html", {"contexts": contexts})

@login_required
def vista_esp(request, job):
    
    conte =  ToDoList.objects.filter(title=job)
    return render(request, "todo_app/index.html", {"contexts": conte})