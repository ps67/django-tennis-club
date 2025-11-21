from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def lien_1(request):
    page = '''
<H1>Hello world!</H1>
<h3><em>Cette page s'affiche pour tous les membres</em></h3>
'''
    return HttpResponse(page)


def members_0(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def members(request):
  allmembers = Member.objects.all().values()
  template = loader.get_template('members.html')
  context = {
    'allmembers': allmembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  member = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'member': member,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

