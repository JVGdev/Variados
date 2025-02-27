for t in range(int(input())):
    decLetters = [ord(i) for i in input()]
    print(decLetters)
    new_string = []
    for i in decLetters:
        if chr(i).isalpha():
            new_string.append(i+3)
        else: new_string.append(i)
    new_string.reverse()
    for i in range(len(new_string)//2, len(new_string)):
        new_string[i] =  new_string[i]-1
    new_string = [chr(i) for i in new_string]
    print("".join(new_string))