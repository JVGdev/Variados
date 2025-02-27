t1, t2, t3 = map(int, input().split(" "))

#print(t1, t2, t3)

if(t2 < t1):
    if (abs(t1)-abs(t2) > abs(t2)-abs(t3) or t3 > t1): print(":)")
    else: print(":(")
elif(t2 > t1):
    if (abs(t2)-abs(t1) < abs(t3)-abs(t2)): print(":)")
    else: print(":(")
else:
    if (t3 >= t1): print(":)")
    else: print(":(")
