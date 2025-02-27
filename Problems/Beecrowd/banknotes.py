total = int(input())
def note_separator(money):
    #notas
    note_qnt = [[100, 0], [50, 0], [20, 0], [10, 0], [5, 0], [2, 0], [1, 0]]
    for i in note_qnt:
        i[1] = money//i[0]
        money -= i[1] * i[0]
        if money == 0: break
    
    return note_qnt

total_portions = note_separator(total)
print(total)
for i in total_portions:
    print(f"{int(i[1])} nota(s) de R$ {i[0]},00")