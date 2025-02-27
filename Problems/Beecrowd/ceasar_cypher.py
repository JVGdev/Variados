for i in range(int(input())):
    code = input()
    step = int(input())

    decripted = []
    alphabet = [chr(i) for i in range(ord("A"), ord("Z")+1)]


    for i in code:
        act_pos = alphabet.index(i)
        new_pos = act_pos - step
        if new_pos < 0: new_pos += 26
        
        decripted.append(alphabet[new_pos])

    print("".join(decripted))
