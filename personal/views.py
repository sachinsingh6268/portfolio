from django.shortcuts import render
from .models import Contact

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact(name=name, email = email, phone = phone, message = message)
        contact.save()
        
    return render(request,'index.html')
