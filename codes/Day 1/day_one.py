#Criar um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.

def temperature_converter():
    fahrenheit = 0
    celsius = 0
    kelvin = 0
    
    unidadeDeMedida = input('Qual a unidade de medida que voce quer utilizar? \n Celsius digite C \n Fahrenheit digite F \n Kelvin digite K ')    
    print('')   
    valorTemperatura = float(input(f'Qual o valor da temperatura?  '))
    
    print('')
    print('')   

        
    if unidadeDeMedida.upper() == 'C':
        kelvin = valorTemperatura + 273.15
        fahrenheit = (kelvin * 1.8) - 459.67         
        return print(f'Os valores são:\n Celsius: {round(valorTemperatura, 2)}\n Fahrenheit: {round(fahrenheit, 2)}\n Kelvin: {round(kelvin, 2)}')
    
    elif unidadeDeMedida.upper() == 'F':
        celsius = 5/9 * (valorTemperatura - 32)
        kelvin = celsius + 273.15
        return print(f'Os valores são:\n Celsius: {round(celsius, 2)}\n Fahrenheit: {round(valorTemperatura, 2)}\n Kelvin: {round(kelvin, 2)}')
    
    elif unidadeDeMedida.upper() == 'K':
        fahrenheit = (valorTemperatura * 1.8) - 459.67
        celsius = 5/9 * (fahrenheit - 32) 
        return print(f'Os valores são:\n Celsius: {round(celsius, 2)}\n Fahrenheit: {round(fahrenheit, 2)}\n Kelvin: {round(valorTemperatura, 2)}')
    
    
        
    
temperature_converter()