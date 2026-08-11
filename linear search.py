def linear_search(numbers, target):
    for index, value in enumerate(numbers):
        if value == target:
            return index

    return -1


numbers = [10, 20, 30, 40, 50]
target = 30

result = linear_search(numbers, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")