from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from mywebapp.models import mywebapp

def index(req):
    # variale = ["name","sirname","parameters"]
    mywebapp1 = mywebapp.objects.all()
    return render(req,'webapp.html',{'mywebapp1':mywebapp1})
    # return HttpResponse("<h2> index </h2>")

# def suraj(req):
#     return render("<h2> suraj </h2>")

# def suraj2(req):
#     return HttpResponse("<h2> suraj 2 </h2>")

# def assets(req):
#     return render(req,'assets/css/style.css')
