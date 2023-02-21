from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import project
# Create your views here.

def projects(request):
    myprojects = project.objects.all().values()
    template = loader.get_template('all_projects.html')
    context = {
        'myprojects': myprojects,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  myprojects = project.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myprojects': myprojects,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())
