for i in range(int(input())):
    nums = [int(i) for i in input()]
    leds = 0
    for i in nums:
        if i in [2, 3, 5]:
            leds += 5
        elif i in [0, 6, 9]:
            leds += 6
        elif i == 1:
            leds += 2
        elif i == 7:
            leds += 3
        elif i == 8:
            leds += 7
        else:
            leds += i
    print(leds, "leds")