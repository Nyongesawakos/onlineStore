from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse
from .models import Member
import xlwt

# Create your views here.

def home(request):
    members= Member.objects.all().values()
    template = loader.get_template('home.html')
    context = {
    'members': members,
  }
    return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  z =request.POST['filename']
  member = Member(firstname=x, lastname=y, filename=z)
  member.save()
  return HttpResponseRedirect(reverse('home.html'))

def delete(request, id):
   member=Member.objects.get(id=id)
   member.delete()
   return HttpResponseRedirect(reverse, ('home'))

def update(request, id):
   member=Member.objects.get(id=id)
   template=loader.get_template('update.html')
   context = {
      'member' : Member
   }
   return HttpResponse(template.render(context, request))
def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Member.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('home.html'))



    