nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / altura ** 2

if ( imc < 18.5 ):
    print (f'Seu imc é de {imc:.2f}, Você está abaixo do peso')

elif ( imc < 25 ):
    print (f'Seu imc é de {imc:.2f}, Você está em um peso ideal (Parabéns)')

elif ( imc < 30 ):
    print (f'Seu imc é de {imc:.2f}, Você está levemente acima do peso')

elif ( imc < 35 ):
    print (f'Seu imc é de {imc:.2f}, Você está com obesidade grau 1')

elif ( imc < 40 ):
    print (f'Seu imc é de {imc:.2f}, Você está com obesidade grau 2 (severa)')

elif ( imc > 40 ):
    print (f'Seu imc é de {imc:.2f}, Você está com obesidade 3 (móbida)')








