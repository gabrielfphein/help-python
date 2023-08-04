

cont = 0
resultado = 0
n = 1000

while cont != n:

    resultado = resultado + 1/(2**cont)

    cont = cont + 1

print(resultado)

x = int(input("Digite um número inteiro: "))

if x < 0:
   resp1 = "negativo"
else:
    resp1 = "positivo"
    
if x % 2 == 0:
    resp2 = "par"
else: 
    resp2 = "impar"
    

print("O número {} é {} e {}.".format(x, resp1, resp2))



var1 = 12

var2 = 30

var3 = var1 + var2

print(var3)

var3 = var3 / 2

print(var3)

x = 10
y = 4.2

num = float(input("Digite um número a seguir: "))

print(num > x*y, num <= x + y, num*y != x*y)
print(num == x, num == y, num == x + y)
print(2 == "2", False, 2.0 == 2)
print(num == x*y, num*y == x*y, y > x + num) # correto

a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

if a > b and a > c:

  resposta = a % 2 == 0

elif b > a and b > c:

  resposta = b % 2 == 0

else:

  resposta = c % 2 == 0

print(resposta)