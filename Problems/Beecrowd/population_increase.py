for i in range(int(input())):
    a, b, ga, gb = map(float, input().split(" "))
    year = 0

    while a <= b and year <= 100:
        a = (a * (1+(ga/100)))//1
        if gb != 0:
            b = (b * (1+(gb/100)))//1
        year += 1

    if year > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{year} anos.") 