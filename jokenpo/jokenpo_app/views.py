from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')         

def resultado(request):
    escolha_usuario = request.POST.get('jogada')
    
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_computador = random.choice(opcoes)
    
    if escolha_usuario == escolha_computador:
        resultado = 'Empate!'
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        resultado = 'Você venceu!'
    else:
        resultado = 'Computador venceu!'    

    contexto = {
        'escolha_usuario': escolha_usuario,
        'escolha_computador': escolha_computador,
        'resultado': resultado,
    }    

    return render(request, 'resultado.html', contexto)      