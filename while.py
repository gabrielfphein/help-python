numero_sorteado = 15

numero_escolhido = int(input('informe um numero de 1 a 15'))

while numero_escolhido != numero_sorteado:
    print('voce errou o numero, tente novamente')
    numero_escolhido = int(input('informe um numero de 1 a 15'))
print('parabens voce acertou')
