numbers = [10,20,30,40,10]
# print(type(numbers))
print(numbers[0])
print(numbers[1])
print(numbers[2])
# print(numbers[4])
print(len(numbers))
numbers[1] = 15
print(numbers)

numbers.append(50)
print(numbers)

numbers.insert(2, 20)
print(numbers)

c = numbers.pop()
print(c)
print(numbers)

numbers.remove(15)
print(numbers)

val = numbers.index(30)
print(val)