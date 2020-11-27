from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from myapp.models import *
def show_about_page(request):
    print("hello")
    name='Learncodewith Ekata'
    link='https://www.youtube.com/watch?v=0QukmlPrrUc&t=1061s'
    data={'name':name,'link':link}
    return render(request,"about.html",data)

def show_home_page(request):
    image=Image.objects.all()
    cat=Category.objects.all()
    data={'images':image,'cats':cat}
    return render(request,"home.html",data) 


def show_category_page(request,cid):  
    
    cat=Category.objects.all()
    category=Category.objects.get(pk=cid)
    image=Image.objects.filter(cat=category)

    data={'images':image,'cats':cat}
    return render(request,"home.html",data) 

def home(request):
    return redirect('/home')    