match nota:=int(input()):
    case nota if nota == 0:
        print("E")
    case nota if 0 < nota <= 35:
        print("D")    
    case nota if 35 < nota <= 60:
        print("C")    
    case nota if 60 < nota <= 85:
        print("B")    
    case _:
        print("A")