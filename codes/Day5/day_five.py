# Criar um programa que calcule o fatorial de um número dado.

def funcao_fatorial(n):
    fatorial = 1
    if n < 0:
        return print("Fatorial não definido para números negativos.")   
    
    for i in range(1, n+1):       
        fatorial = fatorial * i
        
        
        
    return print(fatorial)

number = int(input('Entre com um número inteiro'))
funcao_fatorial(number)


#Aprendizado: math.factorial(numero)