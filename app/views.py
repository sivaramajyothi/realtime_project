from django.shortcuts import render

# Create your views here.
def shoping(request):
    return render(request,'shoping.html') 


def shoping2(request):
    return render(request,'shoping2.html') 

def style(request):
    return render(request,'style.html')