# Criar um jogo simples de adivinhar números.
import random

def numero_aleatorio():
    return random.randint(0, 10)

def main():
    print("Seja bem-vindo ao jogo do 'Adivinha o Número'!")
    print('O objetivo é adivinhar qual é o número inteiro entre 0 e 10.')

    while True:
        print('\nAperte 1 para iniciar ou 0 para sair.')
        try:
            opcao = int(input('Sua escolha: '))
            if opcao == 0:
                print('Obrigado por jogar! Até a próxima.')
                break
            elif opcao == 1:
                jogar()
            else:
                print('Opção inválida. Escolha 1 para jogar ou 0 para sair.')
        except ValueError:
            print('Por favor, insira apenas números (0 ou 1).')

def jogar():
    numero_selecionado = numero_aleatorio()
    print('\nUm número foi sorteado! Tente adivinhar.')

    while True:
        try:
            palpite_usuario = int(input('Dê seu palpite entre 0 e 10: '))

            if palpite_usuario < 0 or palpite_usuario > 10:
                print('Seu palpite está fora do range 0 - 10. Tente novamente.')
            elif palpite_usuario == numero_selecionado:
                print('Parabéns! Você acertou!')
                break
            elif palpite_usuario < numero_selecionado:
                print('Você errou! Dica: seu chute está baixo.')
            else:
                print('Você errou! Dica: seu chute está alto.')
        except ValueError:
            print('Por favor, insira um número inteiro válido.')


main()



""" print("Seja bem vindo ao jogo do 'Adivinha o Número'!")
print('O objetivo é adivinhar qual é o número inteiro entre 0 e 10')
print('Aperte 1 para iniciar')
print('Aperte 0 para sair')

opcao = int(input())

def numero_aleatorio():
    sorteio = random.randint(0, 10)  
    return sorteio  

    
def main(opcao):
    numero_selecionado = numero_aleatorio()
    while opcao == 1:
    
        palpite_usuario = 11
        palpite_usuario = int(input('Dê seu palpite entre 0 e 10: '))    
        
        
        if palpite_usuario == numero_selecionado:
            print('Você acertou!')
            break
        elif palpite_usuario < numero_selecionado and palpite_usuario <= 10 and palpite_usuario >= 0:
            print('Você errou! Dica: seu chute esta baixo.')
            print()
            
        elif palpite_usuario > numero_selecionado and palpite_usuario <= 10 and palpite_usuario >= 0:
            print('Você errou! Dica: seu chute esta alto.')
            print()
            
        elif palpite_usuario > 10 or palpite_usuario < 0:
            print('Seu palpite esta fora do range 0 - 10')  
            print()  
        else:
            break    
        
main(opcao) """