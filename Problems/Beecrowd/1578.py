for c in range(m:=int(input())):
    lincol = int(input())

    mat = [[0 for i in range(lincol)] for i in range(lincol)]
    lenght = [0 for i in range(lincol)]


    for i in range(lincol):
        nums = input().split()

        for j in range(lincol):
            act = mat[i][j] = int(nums[j])**2
            if lenght[j]  < str(act).__len__():
                lenght[j] = str(act).__len__()

    print(f"Quadrado da matriz #{c+4}:")
    for i in range(lincol):
        for j in range(lincol):
            for a in range(lenght[j]-str(mat[i][j]).__len__()):
                print(end=" ")
            print(mat[i][j], end="")
            if j+1 < lincol:
                print(end=" ")
        print("")
    if c+1 < m:
        print("")

    """f = open(r"./test.txt", "a")
    f.write(f"Quadrado da matriz #{c+4}:\n")
    for i in range(lincol):
        for j in range(lincol):
            for a in range(lenght[j]-str(mat[i][j]).__len__()):
                f.write(" ")
            f.write(f"{mat[i][j]}")
            if j+1 < lincol:       
                f.write(" ")
        f.write("\n")
    if c+1 < m:
        f.write("\n")
    f.close()"""