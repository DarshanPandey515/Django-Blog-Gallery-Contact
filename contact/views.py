from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact
# Create your views here.


def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email  = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.Name = name
        contact.Email = email
        contact.Subject = subject
        contact.Message = message
        contact.save()
        return render(request,'success.html')
    else:
        return render(request, 'contact.html')
 