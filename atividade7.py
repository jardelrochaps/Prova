notas1 = int(input("Insira quantidade de notas que você quer calcular: "))
soma = 0
for x in range(notas1):
    notas = float(input('insira nota: '))
    soma += notas

resultado = soma / notas1

print("A media aritmética é: ", resultado)