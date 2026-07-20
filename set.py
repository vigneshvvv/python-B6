sample = {1,2,2,4,3,3}
print(sample)

n = set()

sample.add(5)
print(sample)

sample.update([6,8])
print(sample)

sample.remove(8)
print(sample)

sample.discard(10)

removed = sample.pop()
print("Removed number is: ", removed)
print(sample)

# sample.clear()

# sample = list(sample)
# sample = set(sample)

A= {1,2,3,4}
B= {3,4,5,6}

print(A | B)

print(A & B)

print(A - B)

print(A ^ B)
