print("""Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00""")

lista = []
valor = 0

cod100 = ["Cachorro Quente", 1.2]
cod101 = ["Bauru Simples", 1.3]
cod102 = ["Bauru com Ovo", 1.5]
cod103 = ["Hambúrguer", 1.2]
cod104 = ["Cheeseburguer", 1.3]
cod105 = ["Refrigerante", 1]

while True:
    op = int(input("Insira o codiog desejado: "))
    if op == 0:
        for x in lista:
            print("%s - R$%.2f" %(x[0], x[1]))
        print("Valor total R$%.2f" %valor)
        break

    quantidade = int(input("Quantidade: "))

    if op == 100:
        cod100[1] = 1.2 * quantidade
        lista.append(cod100)
        valor += 1.2 * quantidade

    elif op == 101:
        cod101[1] = 1.3 * quantidade
        lista.append(cod101)
        valor += 1.3 * quantidade

    elif op == 102:
        cod102[1] = 1.5 * quantidade
        lista.append(cod102)
        valor += 1.5 * quantidade

    elif op == 103:
        cod103[1] = 1.2 * quantidade
        lista.append(cod103)
        valor += 1.2 * quantidade

    elif op == 104:
        cod104[1] = 1.3 * quantidade
        lista.append(cod104)
        valor += 1.3 * quantidade

    elif op == 105:
        cod105[1] = 1 * quantidade
        lista.append(cod105)
        valor += 1 * quantidade