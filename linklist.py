class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" → ")
            current = current.next

        print("None")


# Create Linked List
linked_list = LinkedList()

# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Connect nodes
linked_list.head = node1
node1.next = node2
node2.next = node3

# Display
linked_list.display()