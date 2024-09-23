idade1 = int(input("Insira quantidade de pessoas: "))
soma = 0
for x in range(idade1):
    idade = float(input('insira sua idade: '))
    soma += idade

resultado = soma / idade1
if resultado <= 26:
    print("Turma jovem")
elif resultado > 26 and resultado <= 60:
    print("Turma adulta")
else:
    print("Turma idosa")


