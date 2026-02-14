numbers = [10, 20, 30, 20, 40, 50]

# first answer
c20 = 0
for number in numbers:
    if number == 20:
        c20 += 1

print(f'there is {c20} times 20')

# second answer
amount = numbers.count(20)
print(f'there is {amount} times 20')

