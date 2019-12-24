i = 0
numbers = []
for num in range(387638, 919124):
    for j in range(1, 6):
        if (int(str(num)[j]) == int(str(num)[j-1])):
            numbers.append(num)

acceptable_number = []

for number in numbers:
    condition = []
    for j in range(1,6):                                            # part 1
        if (int(str(number)[j]) - int(str(number)[j-1])) >= 0:
            condition.append('true')
    if len(condition) == 5:
        acceptable_number.append(number)
        i += 1
acceptable_numbers = set(acceptable_number)


i = 0
new_acceptable = []
for num in acceptable_numbers:
    first_number = list(str(num))
    for j in range(0, 10):
        if first_number.count(str(j)) == 2:                              # part 2
            new_acceptable.append(num)
            i += 1
            
print(len(set(new_acceptable)))