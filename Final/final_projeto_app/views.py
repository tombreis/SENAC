from django.shortcuts import render
from .models import item

# Create your views here.
def home(request):
    produtos = item.objects.all()
    return render(request, 'home.html', {'produtos': produtos}) 

def sobre(request):
    return render(request, 'sobre.html')    

def checkout(request):
    return render(request, 'checkout.html')   