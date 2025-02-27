n = [0]*100
n[0] = float(input())
for i in range(len(n)):
    if i < len(n)-1: n[i+1] = n[i]/2
    print(f"N[{i}] = {n[i]:.4f}")