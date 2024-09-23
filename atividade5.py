int1 = input('Digite o 1º número inteiro: ')
int2 = input('Digite o 2º número inteiro: ')
real = input('Digite um número real: ')

if int1.isdigit() and int2.isdigit():
    resultado1 = (int(int1)*3) + (int(int2)/2)
    resultado2 = ((int(int1)*3) + float(real)) / (int(int2) ** 2)
    resultado3 = int(int2)**3

    print('o produto do triplo do primeiro com metade do segundo é',resultado1)
    print('a soma do triplo do primeiro com o terceiro, dividido pelo segundo ao quadrado é: %.3f'%resultado2)
    print('o segundo elevado ao cubo é', resultado3)
else:
    print('Há algum valor errado em sua operação!')