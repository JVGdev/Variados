oper = input()

matriz = []
for i in range(12):
    linha = []
    for l in range(12):
        linha.append(float(input()))
    matriz.append(linha)

answr = 0
mn=0
for i in range(12):
    for j in range(12):
        if i>j:
            answr += matriz[i][j]
            mn +=1

if oper == "S":
    print(round(answr/mn, 1))
else:
    answr = round(answr/mn, 1)
    print(answr)