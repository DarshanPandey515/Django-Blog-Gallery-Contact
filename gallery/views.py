from django.shortcuts import render
from .models import Imagegallery
# Create your views here.
def gallery(request):
    gallery = Imagegallery.objects.all()
    return render(request,'gallery.html' , {"gallery":gallery})