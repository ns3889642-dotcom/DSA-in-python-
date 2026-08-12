from collections import deque


# ============================================================
# 1. STACK
# ============================================================

class Stack:
    """Stack implementation using Python list."""

    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)


# ============================================================
# 2. QUEUE
# ============================================================

class Queue:
    """Queue implementation using collections.deque."""

    def __init__(self):
        self._items = deque()

    def enqueue(self, value):
        self._items.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items.popleft()

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)


# ============================================================
# 3. LINKED LIST
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly Linked List."""

    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def search(self, value):
        current = self.head

        while current:
            if current.data == value:
                return True
            current = current.next

        return False

    def display(self):
        current = self.head
        result = []

        while current:
            result.append(current.data)
            current = current.next

        return result


# ============================================================
# 4. BINARY SEARCH TREE
# ============================================================

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree implementation."""

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return BSTNode(data)

        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)

        return node

    def search(self, data):
        current = self.root

        while current:
            if current.data == data:
                return True

            if data < current.data:
                current = current.left
            else:
                current = current.right

        return False

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.data)
            self._inorder(node.right, result)


# ============================================================
# 5. BUBBLE SORT
# ============================================================

def bubble_sort(arr):
    """Sort an array using Bubble Sort."""

    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


# ============================================================
# 6. BINARY SEARCH
# ============================================================

def binary_search(arr, target):
    """Binary Search on a sorted array."""

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# ============================================================
# 7. GRAPH - BFS
# ============================================================

def bfs(graph, start):
    """Breadth-First Search."""

    visited = set()
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()

        if vertex in visited:
            continue

        visited.add(vertex)
        result.append(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                queue.append(neighbor)

    return result


# ============================================================
# 8. GRAPH - DFS
# ============================================================

def dfs(graph, start):
    """Depth-First Search."""

    visited = set()
    result = []

    def traverse(vertex):
        if vertex in visited:
            return

        visited.add(vertex)
        result.append(vertex)

        for neighbor in graph.get(vertex, []):
            traverse(neighbor)

    traverse(start)

    return result


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    # Stack
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack:", stack._items)
    print("Popped:", stack.pop())

    # Queue
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("\nQueue:", list(queue._items))
    print("Dequeued:", queue.dequeue())

    # Linked List
    linked_list = LinkedList()
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)

    print("\nLinked List:", linked_list.display())
    print("Search 20:", linked_list.search(20))

    # BST
    bst = BinarySearchTree()

    for value in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(value)

    print("\nBST Inorder:", bst.inorder())
    print("Search 60:", bst.search(60))

    # Sorting
    numbers = [64, 34, 25, 12, 22, 11, 90]

    print("\nOriginal Array:", numbers)
    print("Sorted Array:", bubble_sort(numbers))

    # Binary Search
    sorted_numbers = [10, 20, 30, 40, 50, 60, 70]

    print("\nBinary Search Index:", binary_search(sorted_numbers, 40))

    # Graph
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": [],
        "F": []
    }

    print("\nBFS:", bfs(graph, "A"))
    print("DFS:", dfs(graph, "A"))