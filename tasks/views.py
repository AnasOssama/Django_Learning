from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

# Create your views here.

class newTaskform(forms.Form):
    task = forms.CharField(label="new task", max_length = 15)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html",{
        "tasks" : request.session["tasks"]
    })

def add_task(request):
    if request.method == "POST":
        form = newTaskform(request.POST)
        if form.is_valid():
           task =  form.cleaned_data["task"]
           request.session["tasks"] += [task]
           return HttpResponseRedirect(reverse("tasks:index"))

        else:
            return render(request, "tasks/add_task.html",{
                "form": form
            })


    return render(request, "tasks/add_task.html",{
        "form": newTaskform()
        })
