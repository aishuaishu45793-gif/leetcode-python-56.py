# 128. Linear Search

numbers = [12, 25, 37, 48, 59, 64]
target = 48
found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")