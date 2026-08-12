class Numbers:
    def __init__(self, numbers):
        self.current = 0
        self.numbers = numbers

    def __iter__(self):
        return self

    def __next__(self):
        # if self.current <= self.max_value:
        #     value = self.current
        #     self.current += 1
        #     return value
        # raise StopIteration

        while self.current < len(self.numbers):
            value = self.numbers[self.current]
            self.current += 1
            if value %2 == 0:
                return value
        raise StopIteration
    
# num = Numbers(5)

# for number in num:
#     print(number)

numberList = [10,15,20,25,30]
even_number = Numbers(numberList)

print(even_number)
for number in even_number:
    print(number)