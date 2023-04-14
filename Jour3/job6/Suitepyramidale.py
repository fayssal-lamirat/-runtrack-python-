string = "abcdefghijklmnopqrstuvwxyz" * 10
n=260
rows = int((2*n)**0.5) + 1

for i in range(rows):
    for j in range(i):
        if i*(i-1)//2 + j < n:
            print(string[i*(i-1)//2 + j], end="")
    print()