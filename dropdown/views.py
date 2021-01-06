from django.shortcuts import render
from .models import *

def programming(request):
    program = Programming.objects.all
    return render(request,'index.html',{'program':program})

def course(request):
    program_id = request.GET.get('programming')
    course = Course.objects.filter(programming_id=program_id).order_by('name')
    return render(request,'couse.html',{'course':course})
