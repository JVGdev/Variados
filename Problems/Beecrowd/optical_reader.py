while True:
    rounds = int(input())
    if rounds == 0: break
    for i in range(rounds):
        markings = [int(i) for i in input().split(" ")]
        answers = ["A", "B", "C", "D", "E"]
        alrd_chsn = False
        chsn_answr = "*"
        
        for i in range(len(markings)):
            if markings[i] > 127: pass

            elif alrd_chsn == False:
                alrd_chsn = True
                chsn_answr = answers[i]
            else: chsn_answr = "*"
            
        print(chsn_answr)   
                