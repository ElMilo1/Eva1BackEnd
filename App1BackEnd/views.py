from django.shortcuts import render
from django.http import HttpRequest , HttpResponse

# Create your views here.

def Home(request):
    return render(request,'TemplateEva/Home.html')

def Product1(request):
    data = {
        'img':'zelda1.jpg',
        'name':'The legend of Zelda: Breath of the wild',
        'val':'10'
    }
    return render(request,'TemplateEva/Product.html',data)

def Product2(request):
    data = {
        'img':'zelda2.webp',
        'name':"The legend of Zelda: Link's awakening",
        'val':'8'
    }
    return render(request,'TemplateEva/Product.html',data)

def Product3(request):
    data = {
        'img':'zelda3.jpg',
        'name':'The legend of Zelda: Twilight Princess',
        'val':'10'
    }
    return render(request,'TemplateEva/Product.html',data)