arr = []
arr2 = list()

numbers = [23, 21, 45, 67, 54, 89, 96]

# Add elements to arr
arr.append(32)
arr.append(25)
arr.append(41)

print(arr)
print(arr2)
print(numbers)

# Classical for Loops
for entry in arr:
    print(entry)

# For loop with enumerate()
for (idx, entry) in enumerate(arr):
    print(f"Element {idx} is {entry}")
