# Question: 3.Write a Python program to create a circular linked list and insert nodes at the beginning, end, and a specified position. Also, display the list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head.next
            self.head.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert_at_position(self, data, position):
        if position < 0:
            print("Invalid position")
            return
        new_node = Node(data)
        if position == 0:
            self.insert_at_beginning(data)
            return
        current = self.head
        count = 1
        while current.next != self.head and count < position:
            current = current.next
            count += 1
        if count == position:
            new_node.next = current.next
            current.next = new_node
        else:
            print("Position exceeds list size")

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

# Example usage
list = CircularLinkedList()
list.insert_at_end(5)
list.insert_at_beginning(4)
list.insert_at_end(6)
list.insert_at_position(3, 1)
list.display()  # Output: 4 3 5 6