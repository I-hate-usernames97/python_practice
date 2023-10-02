max_num = [10, 13, 41, 20, 1, 2, 6, 99]
max = 0

for number in max_num:
    if number > max:
        max = number
print(max)


numbers = [2, 2, 3, 3, 4, 4, 4, 5, 5, 1]
uniques = []

for num in numbers:
    if num not in uniques:
        uniques.append(num)
print(uniques)