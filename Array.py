# Data Structures and Algorithms (DSA) in Python

# 1. Array / List
numbers = [10, 20, 30, 40, 50]

print("Array:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])


# 2. Stack - LIFO (Last In, First Out)
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("\nStack:", stack)
print("Popped element:", stack.pop())
print("Stack after pop:", stack)


# 3. Queue - FIFO (First In, First Out)
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print("\nQueue:", queue)
print("Removed element:", queue.popleft())
print("Queue after removal:", queue)


# 4. Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


numbers = [10, 20, 30, 40, 50]
target = 30

result = linear_search(numbers, target)

if result != -1:
    print("\nElement found at index:", result)
else:
    print("\nElement not found")


# 5. Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


numbers = [10, 20, 30, 40, 50]
target = 40

result = binary_search(numbers, target)

if result != -1:
    print("Binary search: Element found at index:", result)
else:
    print("Binary search: Element not found")


# 6. Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


numbers = [50, 20, 40, 10, 30]

print("\nBefore sorting:", numbers)
print("After sorting:", bubble_sort(numbers))


# 7. Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


linked_list = LinkedList()

linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)

print("\nLinked List:")
linked_list.display()