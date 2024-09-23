num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
num3 = int(input('Digite o terceiro número inteiro: '))
num4 = int(input('Digite o quarto número inteiro: '))
num5 = int(input('Digite o quinto número inteiro: '))
num6 = int(input('Digite o sexto número inteiro: '))
num7 = int(input('Digite o sétimo número inteiro: '))
num8 = int(input('Digite o oitavo número inteiro; '))
num9 = int(input('Digite o nono número inteiro: '))
num10 = int(input('Digite o décimo número inteiro: '))

par = 0
impar = 0

numeros = [num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]
for x in (numeros):
    if x % 2 == 0:
        par += 1
    else:
        impar += 1

print('Pares:', par)
print('Impares:', impar)