from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'resume/index.html')

def aboutme(request):
    return render(request, 'resume/aboutme.html')

def project(request):
    return render(request, 'resume/project.html')