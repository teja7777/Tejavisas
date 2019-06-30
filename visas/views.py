from django.shortcuts import render
from .models import Schedule
from visas.forms import contact_form
from django.http import HttpResponseRedirect

# Create your views here.
def contactus(request):
    return render(request,'contactus.html')
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def terms(request):
    return render(request,'terms.html')
def disclaimer(request):
    return render(request,'disclaimer.html')
def cancel(request):
    return render(request,'cancel.html')
def dec(request):
    return render(request,'dec.html')
def policy(request):
    return render(request,'policy.html')


def schedule(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Schedule(email=email_r,subject=subject_r,message=message_r)
        c.save()
        return render(request,'schedule.html')
    else:
        return render(request,'schedule.html')


def contact1(request):
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('contactform')
    else:
        form = contact_form()
    return render(request,'contact.html',{'form':form})