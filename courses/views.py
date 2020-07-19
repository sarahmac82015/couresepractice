from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all()
        }
    return render(request, 'newcourse.html', context)

def create(request):
    # CREATE THE COURSE
    errors = Course.objects.validate(request.POST)
    if len(errors):
        for (key, value) in errors.items():
            messages.error(request, value)
        return redirect('/courses/create')

    Course.objects.create(
        name = request.POST['name'],
        description = request.POST['description']
    )
    return redirect('/courses')

def delete(request,id):
    if request.method == "GET":
        context = {
            "course": Course.objects.get(id=id)
    }
        return render(request,'deletecourse.html', context)

    if request.method == "POST":
        course = Course.objects.get(id=id)
        course.delete()
        return redirect("/courses")