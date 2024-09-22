med1 = input('Digite a 1ª média: ')
med2 = input('Digite a 2ª média: ')
med3 = input('Digite a 3ª média: ')
med4 = input('Digite a 4ª média: ')
med5 = input('Digite a 5ª média: ')

if med1.isdigit() and med2.isdigit() and med3.isdigit() and med4.isdigit() and med5.isdigit():
    resultado = (int(med1) + int(med2) + int(med3) + int(med4) + int(med5)) / 5
    print('Sua média é:', resultado)

else:
    print('Algum dos valores não é um número!')