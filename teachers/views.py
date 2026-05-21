from django.shortcuts import render

# Create your views here.

from .models import Teacher

def bosh_sahifa(request):
    ustozlar = Teacher.objects.all()
    return render(request, 'bosh_sahifa.html',{'ustozlar': ustozlar})