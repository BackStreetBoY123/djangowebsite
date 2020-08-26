from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
# Create your views here.
def index(req):
    return render(req,'index.html')

