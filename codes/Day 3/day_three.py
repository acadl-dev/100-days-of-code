#Desenvolver uma calculadora simples com as operações básicas (+, -, *, /).

def calculadora():
    escolha_usuario = 0
    
    
    while (escolha_usuario != 5 ):        
        print("\n=== Calculadora Simples ===")
        print("Escolha uma das opções:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")
        print("===========================")
        escolha_usuario = int(input())
        print()
        print()
    
        if escolha_usuario == 1:
            print('Opção SOMA selecionada.')
            primeira_parcela = float(input('Digite o valor da primeira parcela:'))
            segunda_parcela = float(input('Digite o valor da segunda parcela:'))
            total = primeira_parcela + segunda_parcela
            print(f'O total desta soma é {total}')
            print()
            
        elif escolha_usuario == 2:
            print('Opção SUBTRAÇÃO selecionada.')
            minuendo = float(input('Digite o valor do minuendo:'))
            subtraendo = float(input('Digite o valor do subtraendo:'))
            resto = minuendo - subtraendo
            print(f'A diferença desta subtração é {resto}')
            print()
            
        elif escolha_usuario == 3:
            print('Opção MULTIPLICAÇÃO selecionada.')
            multiplicando = float(input('Digite o valor do multiplicando:'))
            multiplicador = float(input('Digite o valor do multiplicador:'))
            produto = multiplicando * multiplicador
            print(f'O produto desta multiplicação é {produto}')
            print()
            
        elif escolha_usuario == 4:
            print('Opção DIVISÃO selecionada.')
            dividendo = float(input('Digite o valor do dividendo:'))
            divisor = float(input('Digite o valor do divisor:'))
            quociente = dividendo / divisor
            print(f'O quociente desta divisão é {quociente}')
            print()
            
        elif escolha_usuario == 5:
            return print('Programa finalizado!')
        
        else:
            print('Opção inválida, tente de novo!')  
            print()  
    
    
    
calculadora()