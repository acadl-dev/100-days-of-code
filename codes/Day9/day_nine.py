# Implementar uma função para calcular o MDC e o MMC de dois números.
from colorama import init, Fore, Back, Style
init(autoreset=True)

cor_texto_verde = '\x1b[32m'
fechamento = '\033[0m'

def main():
    print(Back.YELLOW +'ENCONTRE O MDC E O MMC!' )
      
    
    primeiro_numero = int(input(Fore.RED + Back.MAGENTA + 'Entre com o primeiro valor inteiro: '))
    segundo_numero = int(input('Agora entre com segundo valor: '))
    
    print()
    mdc = 0
    mmc = 0    
    
    if primeiro_numero > segundo_numero:
        mdc = maximo_divisor_comum(primeiro_numero, segundo_numero)
    elif segundo_numero > primeiro_numero:
        mdc = maximo_divisor_comum(segundo_numero, primeiro_numero)
    
        
    mmc = minimo_multiplo_comum(primeiro_numero, segundo_numero)
    
    print(f'Referente aos valores informados o  MDC é: {cor_texto_verde}{mdc}{fechamento} e o MMC é: {cor_texto_verde}{mmc}{fechamento}')
    
    
def maximo_divisor_comum(pv, sv):
    #algoritmo de euclides
    while sv != 0:        
     pv, sv = sv, pv % sv 
      
    return pv

def minimo_multiplo_comum(pv, sv):
    mmc = (pv * sv)/maximo_divisor_comum(pv, sv)    
    
    return round(mmc) 
    


main()