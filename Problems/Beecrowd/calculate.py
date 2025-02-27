code1, num1, unit1 = map(float, input().split(" "))
code2, num2, unit2 = map(float, input().split(" "))
print(f"VALOR A PAGAR: R$ {(num1*unit1)+(num2*unit2):.2f}")