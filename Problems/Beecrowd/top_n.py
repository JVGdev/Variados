pos = int(input())
tops = [1, 3, 5, 10, 25, 50, 100]
for i in tops:
    if pos <=i:
        print(f"Top {i}")
        break