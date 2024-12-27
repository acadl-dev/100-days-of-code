import re  

def contador_de_palavras(n):
    n = n.lower()  
    n = re.sub(r'[^\w\s]', '', n)  
    lista_palavras = n.split()  
    dicionario_contagem = {}  

    for palavra in lista_palavras:
        if palavra in dicionario_contagem:  
            dicionario_contagem[palavra] += 1  
        else:
            dicionario_contagem[palavra] = 1  

    return dicionario_contagem  


frase_entrada = input('Entre com a frase: ')

resultado = contador_de_palavras(frase_entrada)
print('')
print("Frequência de palavras:")
for palavra, contagem in resultado.items():
    print(f"{palavra}: {contagem}")
