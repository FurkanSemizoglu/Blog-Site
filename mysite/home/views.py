from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    return render(request,'pages/index.html')

def search(request):
    return render(request,'pages/search.html')


def blog(request):
    blogs = Blog.objects.all()
    context = {"blogs" : blogs}
    return render(request,'pages/blog.html',context)