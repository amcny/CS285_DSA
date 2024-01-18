# Question: 3.Write a Python program to create a circular linked list and insert nodes at the beginning, end, and a specified position. Also, display the list.


'''   Here's a kid-friendly explanation of the code:  

  Imagine a train with special carriages:  

- Each carriage holds a piece of information (like a number or a word).
- Each carriage has a special arrow that points to the next carriage, creating a circle.
- The train's conductor (the `CircularLinkedList`) keeps track of the first carriage (the `head`).

  When we want to add a new carriage:  

  1. Adding to the Beginning:  
   - Imagine a new carriage arrives at the station.
   - The conductor quickly attaches it to the front of the train, right before the first carriage.
   - The conductor updates their notes to remember the new carriage as the first one.
   - The new carriage's arrow points to the old first carriage, keeping the circle intact.

  2. Adding to the End:  
   - The conductor hops on the train and rides it all the way to the back.
   - They attach the new carriage to the very last one.
   - The new carriage's arrow points to the first carriage, completing the circle.

  3. Adding at a Specific Position:  
   - The conductor counts the carriages until they reach the desired spot.
   - They carefully insert the new carriage between two existing ones, like fitting a puzzle piece.
   - They make sure the arrows are pointing in the right directions to maintain the circle.

  When we want to see the whole train:  

   - The conductor starts at the first carriage and points to each one in turn, calling out its information.
   - They keep going until they circle back to the first carriage, making sure to show every carriage in the loop.

  That's how this special circular train, or circular linked list, works!  '''


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