# Question: 2. Implement a Python program for a doubly linked list that allows deleting nodes from the beginning, end, and a specified position. Display the list after each deletion operation.


''' Here's a kid-friendly explanation of the code: 

 Imagine our number train again! Now we're going to learn how to remove cars from different spots. 

 1. Removing the First Car: 
   - If the train is empty, we can't remove anything, so we say "The train is empty!"
   - If there's only one car, we just make the train empty by removing the first (and only) car.
   - If there are more cars, we make the second car the new first car, and we unlink the first car from the rest of the train.

 2. Removing the Last Car: 
   - If the train is empty, we can't remove anything, so we say "The train is empty!"
   - If there's only one car, we just make the train empty by removing the last (and only) car.
   - If there are more cars, we make the second-to-last car the new last car, and we unlink the last car from the rest of the train.

 3. Removing a Car from the Middle: 
   - First, we check if the position where we want to remove a car is valid. If it's not, we say "Invalid position!"
   - If the train is empty, we can't remove anything, so we say "The train is empty!"
   - If we want to remove the first or last car, we already know how to do that, so we use those methods.
   - Otherwise, we find the car that's currently in the position we want to remove.
   - We carefully unlink the car we want to remove by connecting the car in front of it with the car behind it, like taking a link out of a chain.

 That's it! Now you can remove cars from your number train wherever you want! '''

# Virtual Visualization : 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_at_position(self, data, position):
        if position < 1:
            print("Invalid position")
            return

        new_node = Node(data)

        if position == 1:
            self.insert_at_beginning(data)
            return

        current = self.head
        current_position = 1

        while current is not None and current_position < position - 1:
            current = current.next
            current_position += 1

        if current is None:
            print("Position exceeds list size")
            return

        new_node.next = current.next
        current.next.prev = new_node
        current.next = new_node
        new_node.prev = current

    def print_forward(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def print_backward(self):
        current = self.tail
        while current is not None:
            print(current.data, end=" ")
            current = current.prev
        print()

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_at_end(self):
        if self.tail is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete_at_position(self, position):
        if position < 1:
            print("Invalid position")
            return

        if self.head is None:
            print("List is empty")
            return

        current = self.head
        current_position = 1

        while current is not None and current_position < position - 1:
            current = current.next
            current_position += 1

        if current is None or current.next is None:  # Handle edge cases
            if position == 1:
                self.delete_at_beginning()
            elif position == self.get_length():
                self.delete_at_end()
            else:
                print("Position exceeds list size")
            return

        current.next.prev = current.prev
        current.prev.next = current.next

# Example usage
dll = DoublyLinkedList()
dll.insert_at_beginning(4)
dll.insert_at_end(8)
dll.insert_at_position(6, 2)

print("Original list:")
dll.print_forward()

dll.delete_at_beginning()
print("After deleting from beginning:")
dll.print_forward()

dll.delete_at_end()
print("After deleting from end:")
dll.print_forward()
