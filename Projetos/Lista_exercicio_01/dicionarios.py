# 1 - Esse é meu primeiro dicionário - Criando Dicionário
livro = {
    "titulo": "Grimorio Um",
    "paginas": 666,
    "autor": "Fausto Enir",
} 

# 2 - Esse é meu dicionário de dicionários
estante = {
    "livro1": livro,
    "livro2": {    
        "titulo": "Grimorio Dois",
        "paginas": 444,
        "autor": "Norma Rocha",
    }    
}

print(livro.get("paginas")) # Este é um jeito de acessar itens
print(livro["paginas"]) # Este é outro jeito de acessar itens
print(estante["livro2"]["autor"]) # Este é um jeito de acessar itens dentro do dicionário dentro de outro dicionário

livro.update({"paginas": 999}) # Atualiza um valor dentro do dicionário

# 3 - Removendo itens do dicionário

livro.pop("autor") # Remove o item autor de livro
del livro["titulo"] # Remove o item titulo de livro


# 4 - Zerando valor de uma chave

livro["autor"] = ""

print(livro.keys()) # O método key() retorna as chaves
value # O método values() retorna os valores