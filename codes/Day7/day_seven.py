# Verificar se uma palavra é um palíndromo.

def palindrome_check(n):
    
    palavra_minuscula = n.lower()    
    palavra_inversa = palavra_minuscula[::-1]     
    return palavra_minuscula == palavra_inversa


def main():
    entrada_usuario = input('Entre com uma palavra: ')
    if palindrome_check(entrada_usuario):
        print('Esta palavra é palíndroma!')
    else:
        print('Esta palavra não é palíndroma!')


main()


""" def palindrome_check(n):
    
    palavra_minuscula = n.lower()    
    palavra_inversa = ''.join(reversed(palavra_minuscula))    
    
    if palavra_minuscula == palavra_inversa:
        return True
    elif palavra_minuscula != palavra_inversa:
        return False
    

entrada_usuario = input('Entre com uma palavra: ')


if palindrome_check(entrada_usuario) == True:
    print('Esta palavra é palíndroma!')
else:
    print('Esta palavra não é palíndroma!') """
