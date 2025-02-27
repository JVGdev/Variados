# Montar grafo

grafo = {
    "a": [1, 2, 3, 4, 5, 6, 7 , 8],
    "b": [1, 2, 3, 4, 5, 6, 7 , 8],
    "c": [1, 2, 3, 4, 5, 6, 7 , 8],
    "d": [1, 2, 3, 4, 5, 6, 7 , 8],
    "e": [1, 2, 3, 4, 5, 6, 7 , 8],
    "f": [1, 2, 3, 4, 5, 6, 7 , 8],
    "g": [1, 2, 3, 4, 5, 6, 7 , 8],
    "h": [1, 2, 3, 4, 5, 6, 7 , 8]
}
gambiarra = ["a", "b", "c", "d", "e", "f", "g", "h"]
#a, b = input().split(" ")
a = "e2"
b = "e4"

act_pos = a
print(grafo)


#verificar o que é mais facil andar pro lado ou pra frente
while act_pos != b:
    des_column = gambiarra.index(b[0])
    act_column = gambiarra.index(act_pos[0])

    if act_pos[1]%2 >

