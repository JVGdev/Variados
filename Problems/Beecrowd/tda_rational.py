#study the time limit

for i in range(int(input())):
    fracs= input().split(" ")

    frac1 = [int(fracs[0]), int(fracs[2])]
    operator = fracs[3]
    frac2 = [int(fracs[4]), int(fracs[6])]

    match operator:
        case "+":
            new_frac = [(frac1[0]*frac2[1] + frac2[0]*frac1[1]), (frac1[1]*frac2[1])]
        case "-":
            new_frac = [(frac1[0]*frac2[1] - frac2[0]*frac1[1]), (frac1[1]*frac2[1])]
        case "*":
            new_frac = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
        case "/":
            new_frac = [frac1[0] * frac2[1], frac1[1] * frac2[0]]  


    a = new_frac[0]
    b = new_frac[1]
    simpl_frac = [a, b]
    for i in range(100):
        try:
            a = simpl_frac[0]
            b = simpl_frac[1]
            mmc = [x for x in range(2, (a*b)+1) if a%x==0 and b%x==0][0]
            simpl_frac[0] = a // mmc
            simpl_frac[1] = b // mmc
        except:
            break
        
        
    print(f"{new_frac[0]}/{new_frac[1]} = {simpl_frac[0]}/{simpl_frac[1]}")

