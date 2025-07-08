import random

def jogo_da_forca():

    palavras = "python programacao computador algoritmo desenvolvimento"
    palavra_secreta = random.choice(palavras.split()).upper()
    

    letras_acertadas = "_" * len(palavra_secreta)
    letras_erradas = ""
    tentativas = 6
    
    print("Bem-vindo ao Jogo da Forca!")
    print(" ".join(letras_acertadas))
    
    while True:
        letra = input("\nDigite uma letra: ").upper()
        
    
        if letra in letras_acertadas or letra in letras_erradas:
            print(f"Você já tentou a letra {letra}.")
            continue
            

        if letra in palavra_secreta:
            print(f"Acertou! A letra {letra} está na palavra.")
            # Atualiza as letras acertadas
            nova_palavra = ""
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    nova_palavra += letra
                else:
                    nova_palavra += letras_acertadas[i]
            letras_acertadas = nova_palavra
        else:
            print(f"Errou! A letra {letra} não está na palavra.")
            letras_erradas += letra
            tentativas -= 1
            
        # Mostra o estado atual do jogo
        print("\nPalavra: " + " ".join(letras_acertadas))
        print(f"Letras erradas: {" ".join(letras_erradas)}")
        print(f"Tentativas restantes: {tentativas}")
        
        # Verifica se o jogador ganhou
        if "_" not in letras_acertadas:
            print("\nParabéns! Você acertou a palavra!")
            break
            
        # Verifica se o jogador perdeu
        if tentativas == 0:
            print(f"\nGame Over! A palavra era: {palavra_secreta}")
            break

# Inicia o jogo
jogo_da_forca()