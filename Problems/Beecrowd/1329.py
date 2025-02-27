while True:
    max = int(input())
    if max == 0: break
    lista = list(map(int, input().split(" ")))
    mary = lista.count(0)
    john = lista.count(1)

    print(f"Mary won {mary} times and John won {john} times")