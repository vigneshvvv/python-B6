number = [10,20,30,40]

iterator = iter(number)
# print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))

while True:
    try:
        num = next(iterator)
        print(num)
    except StopIteration:
        break