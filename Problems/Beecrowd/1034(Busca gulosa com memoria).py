# Problema de Runtime #

for i in range(int(input())):
    max_blocks, all_size = map(int, input().split(" "))

    blocks = [int(i) for i in input().split(" ")]
    #blocks = list(map(int, input().split(" ")))
    memory = [0]*(all_size+1)

    for actual_max in range(1, all_size+1):
        blockCount = actual_max

        for actual_block in [c for c in blocks if c<= actual_max]:
            if memory[actual_max-actual_block]+1 <= blockCount:
                blockCount = memory[actual_max-actual_block]+1
            
        memory[actual_max] = blockCount

    print(memory[all_size])
    print(memory)


