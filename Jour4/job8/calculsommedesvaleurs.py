L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

sum_of_evens = 0

for num in L:
    if num % 2 == 0:
        sum_of_evens += num

print(sum_of_evens)
