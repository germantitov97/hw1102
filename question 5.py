numbers = [10, 20, 30, 20, 40, 50]
# removing only the first 20
_20remove = numbers.remove(20)
print(numbers)

# removing all 20 from the list
numbers2 = [10, 20, 30, 20, 40, 50]
for i in numbers2:
    if i == 20:
        numbers2.remove(i)
print(numbers2)