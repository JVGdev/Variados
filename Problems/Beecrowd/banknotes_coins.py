from decimal import *

total = Decimal(input())

def note_separator(money):

    #notas
    note_qnt = [[100, 0], [50, 0], [20, 0], [10, 0], [5, 0], [2, 0]]
    for i in note_qnt:
        i[1] = money//i[0]
        money -= int(i[1] * i[0])
        if money == 0: break

    #Moedas
    coin_qnt = [[1.00, 0], [0.50, 0], [0.25, 0], [0.10, 0], [0.05, 0], [0.01, 0]]
    for i in coin_qnt:

        i[1] = (Decimal(money)+Decimal(0.001))//Decimal(i[0])
        money -= Decimal(i[1]) * Decimal(i[0])
        if money == 0: break
    
    
    return note_qnt, coin_qnt

total_portions = note_separator(total)
print("NOTAS:")
for i in total_portions[0]:
    print(f"{int(i[1])} nota(s) de R$ {i[0]:.2f}")
print("MOEDAS:")
for i in total_portions[1]:
    print(f"{int(i[1])} moeda(s) de R$ {i[0]:.2f}")

print(total_portions)
