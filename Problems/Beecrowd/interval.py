intervalos = ["[0,25]", "(25,50]", "(50,75]", "(75,100]"]
intervalo = 0
num = float(input())

if 100 >= num >= 0:
    for i in range(1, 5):
        if num > 25*i:
            intervalo += 1
            
    print(f"Intervalo {intervalos[intervalo]}")

else:
    print("Fora de intervalo")
