from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def areadoaluno(request):
    return render(request, 'AreaDoAluno.html')

def planos(request):
    return render(request, 'Planos.html')

def sobrenos(request):
    return render(request, 'SobreNos.html')

def trabalhe(request):
    return render(request, 'TrabalheConosco.html')

