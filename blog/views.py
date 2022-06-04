from django.shortcuts import render
from .models import Post,Knowme

# Create your views here.

def home(request):
    return render(request,'home.html')

def blog(request):
    posts = Post.objects.all()
    return render(request,'blog.html',{"posts":posts})

def detail(request,slug):
    posts= Post.objects.filter(Post_Slug=slug)
    return render(request,'detail.html',{"posts":posts})


def services(request):
    return render(request,'services.html')


def about(request):
    itsme = Knowme.objects.all()
    return render(request,'about.html',{"itsme":itsme})

def success(request):
    return render(request,'success.html')

def detail(request,slug):
    post = Post.objects.filter(Post_Slug=slug)
    return render(request,'detail.html', {"post":post})