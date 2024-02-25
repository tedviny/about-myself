from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ContactForm
from porfolio.models import MessageContact
from django.utils import timezone


# Create your views here.
def index(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            new_message = MessageContact(email=email, message=message,date=timezone.now())
            new_message.save()
            return HttpResponseRedirect('')
        else :
            form = ContacForm()
            return render(request, 'index.html',{'form':form})
    return render(request, 'index.html')

