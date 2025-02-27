dim = [1, 1]

while dim[0] != 0:
        # PLanks go like (4 with 1, 3 with 2) or else: dont print
        dim = [int(i) for i in input().split(" ")]
        dim.sort(reverse=True)
        if dim[0] == 0 and dim[1] == 0:
            break
        width = int(input())
        num = int(input())
        planks =  [int(i) for i in input().split(" ")]
        planks.sort(reverse=True)
        #print(dim, width, num, planks)

        total_area = dim[0]*dim[1]*100

        total = 0
        total_area_used = 0
        biggest_plank = planks[0]

        for i in planks:
            if i == biggest_plank and biggest_plank == dim[0]:
                total+=1
                total_area_used += biggest_plank * width
            else:
                try:
                    a_p_i = planks.index(biggest_plank-i)
                    #print(a_p_i, i, planks)
                    other_plank = planks[a_p_i]

                    total+=2
                    total_area_used += (i + other_plank) * width
                    planks.remove(planks[a_p_i])
                except:
                    pass
            
            if total_area == total_area_used:
                print(total)
                break

        if total_area < total_area_used or total_area > total_area_used:
            print("impossivel")

        #print(f"Area:", total_area, "area usada:", total_area_used, "Tabuas:", total)

