import tkinter as tk
from tkinter import messagebox
import random

class JogoTesouro:
    def __init__(self, root):
        self.root = root
        self.root.title("Caça ao Tesouro")
        self.root.geometry("500x600")
        
        # Variáveis do jogo
        self.tamanho_grid = 5
        self.tesouro_linha = random.randint(0, self.tamanho_grid-1)
        self.tesouro_coluna = random.randint(0, self.tamanho_grid-1)
        self.tentativas = 0
        self.max_tentativas = 5
        
        # Interface
        self.criar_interface()
        
    def criar_interface(self):
        # Frame principal
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack(expand=True, fill=tk.BOTH)
        
        # Título
        tk.Label(
            self.main_frame, 
            text="Caça ao Tesouro", 
            font=("Arial", 18, "bold")
        ).pack(pady=10)
        
        # Instruções
        tk.Label(
            self.main_frame, 
            text=f"Encontre o tesouro em no máximo {self.max_tentativas} tentativas!",
            font=("Arial", 12)
        ).pack(pady=5)
        
        # Grid de botões
        self.frame_grid = tk.Frame(self.main_frame)
        self.frame_grid.pack(pady=20)
        
        self.botoes = []
        for linha in range(self.tamanho_grid):
            linha_botoes = []
            for coluna in range(self.tamanho_grid):
                btn = tk.Button(
                    self.frame_grid,
                    text=" ", 
                    width=4, 
                    height=2,
                    font=("Arial", 12),
                    command=lambda l=linha, c=coluna: self.clicar_celula(l, c)
                )
                btn.grid(row=linha, column=coluna, padx=3, pady=3)
                linha_botoes.append(btn)
            self.botoes.append(linha_botoes)
        
        # Contador de tentativas
        self.label_tentativas = tk.Label(
            self.main_frame, 
            text=f"Tentativas: {self.tentativas}/{self.max_tentativas}",
            font=("Arial", 12)
        )
        self.label_tentativas.pack(pady=10)
        
        # Botão de reiniciar
        tk.Button(
            self.main_frame,
            text="Reiniciar Jogo",
            font=("Arial", 12),
            command=self.reiniciar_jogo
        ).pack(pady=10)
    
    def clicar_celula(self, linha, coluna):
        # Verificar se o jogo já acabou
        if self.tentativas >= self.max_tentativas:
            return
            
        # Incrementar tentativas
        self.tentativas += 1
        self.label_tentativas.config(text=f"Tentativas: {self.tentativas}/{self.max_tentativas}")
        
        # Verificar se encontrou o tesouro
        if linha == self.tesouro_linha and coluna == self.tesouro_coluna:
            self.botoes[linha][coluna].config(text="💎", bg="gold", state=tk.DISABLED)
            messagebox.showinfo("Parabéns!", "Você encontrou o tesouro!")
            self.desabilitar_botoes()
            return
        
        # Calcular distância do tesouro
        distancia = ((self.tesouro_linha - linha)**2 + (self.tesouro_coluna - coluna)**2)**0.5
        
        # Dar feedback visual
        if distancia <= 1.5:
            cor = "red"
            dica = "Pegando fogo!"
        elif distancia <= 2.5:
            cor = "orange"
            dica = "Muito quente!"
        elif distancia <= 3.5:
            cor = "yellow"
            dica = "Quente"
        elif distancia <= 4:
            cor = "light blue"
            dica = "Morno"
        else:
            cor = "blue"
            dica = "Frio"
            
        self.botoes[linha][coluna].config(text="X", bg=cor, state=tk.DISABLED)
        
        # Verificar se acabaram as tentativas
        if self.tentativas >= self.max_tentativas:
            self.botoes[self.tesouro_linha][self.tesouro_coluna].config(text="💎", bg="gold")
            messagebox.showinfo("Fim de Jogo", 
                              f"Suas tentativas acabaram! O tesouro estava em ({self.tesouro_linha+1}, {self.tesouro_coluna+1})")
            self.desabilitar_botoes()
        else:
            messagebox.showinfo("Dica", dica)
    
    def desabilitar_botoes(self):
        for linha in self.botoes:
            for btn in linha:
                btn.config(state=tk.DISABLED)
    
    def reiniciar_jogo(self):
        # Resetar variáveis do jogo
        self.tesouro_linha = random.randint(0, self.tamanho_grid-1)
        self.tesouro_coluna = random.randint(0, self.tamanho_grid-1)
        self.tentativas = 0
        self.label_tentativas.config(text=f"Tentativas: {self.tentativas}/{self.max_tentativas}")
        
        # Resetar botões
        for linha in self.botoes:
            for btn in linha:
                btn.config(text=" ", bg="SystemButtonFace", state=tk.NORMAL)

# Iniciar o jogo
if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoTesouro(root)
    root.mainloop()