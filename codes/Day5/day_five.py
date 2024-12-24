# Escrever um gerador de números da sequência de Fibonacci.

""" def fibonacci_function(n):
    fibo_list = [0, 1]     
    k = 0
    
    while (fibo_list[k] <= n):              
        fibo_list.append(fibo_list[k] + fibo_list[k+1])
        k += 1        
        
    fibo_list.pop()
    fibo_list.pop()    
    return print(fibo_list)

fibonacci_function(55) """

def fibonacci_function(n):
    if n < 0:
        return []
    fibo_list = [0, 1]
    
    while fibo_list[-1] + fibo_list[-2] <= n:
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
        
    return print(fibo_list)

entrada = int(input('Digite um valor para retornar a sequencia de Fibonacci até ele: '))
fibonacci_function(entrada)
    