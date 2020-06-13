from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class Home(DetailView):
#     model= Item
#     template_name="home.html"
#     context_object_name= 'form'


def Home(request):
    items= Item.objects.all()
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request,'home.html',{'items':items,'user':username})

def Detail(request,sn):
    item= Item.objects.filter(pk=sn)
    return render(request,'detail.html',{'item':item[0]})


def Cart(request):
    return render(request,'cart.html')


def Buy(request,sn):
    item = Item.objects.filter(pk=sn)
    return render(request,'buy.html',{'item':item[0]})

def SignUp(request):
    if request.method=="POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})
