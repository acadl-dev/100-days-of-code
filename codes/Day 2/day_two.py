#Implementar um verificador de números primos.

def algoritmo_crivo_de_eratostenes(n):
    lista_de_numeros = [True] * (n+1)
    contador = 2
    
    while (contador * contador <= n):
        if (lista_de_numeros[contador] == True):
            for i in range(contador * contador, n + 1, contador):
                lista_de_numeros[i] = False
        contador += 1
    resultado_primos = [contador for contador in range(2, n + 1) if lista_de_numeros[contador]]
    return print(resultado_primos)
        
algoritmo_crivo_de_eratostenes(30)

#sintaxe básica do range: range(start, stop, step); 
# start é a posição de início da sequência (por padrão é 0); 
# stop é o limite (exclusivo) da sequência; 
# step é o valor de incremento da sequência (por padrão é 1).