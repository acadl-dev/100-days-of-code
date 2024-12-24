# Escrever uma função que inverta uma string.

def inverter_string(n):    
    string_invertida = ''.join(reversed(n))    
    string_invertida2 = n[::-1]
    
    return print(f"Com o método reversed: '{string_invertida}', com a técnica de fatiamento: '{string_invertida2}'.")

n = str(input('Insira uma string ou usa frase:   '))
    
inverter_string(n)