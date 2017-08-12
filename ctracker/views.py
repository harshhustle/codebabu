from django.shortcuts import render
from django.template.context import RequestContext

def index(request):
    return render(request, 'base.html')

