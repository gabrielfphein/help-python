
for variavel in range(1, 12, 3):
    print(variavel)

    nota1 = float(input('informe sua nota 1'))
    nota2 = float(input('informe sua nota 2'))
    nota3 = float(input('informe sua nota 3'))
#### utilizaçao para diminuir a repetiçao

soma = 0
for i in range(1,4):
    nota= float(input(f'informe a sua notaa {i}:'))
    soma = soma + nota
    print(soma/3)