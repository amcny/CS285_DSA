# Question: 1. Write a Python program to create a doubly linked list and insert nodes at the beginning, end, and a specified position. Also, display the list in both forward and backward directions.


''' Here's a kid-friendly explanation of the code: 

 Imagine a train with special cars that can hold numbers. 

-  Each car is like a "node,"  and it can carry a single number (called "data").
-  Each car also has two special handles:  one pointing to the car in front (called "next") and one pointing to the car behind (called "prev").
-  The whole train is like a "doubly linked list,"  and we can add cars to the front, back, or anywhere in between.

 Here's how the code works to build and use this train: 

 1. Creating the Train: 
   - We start by making a blueprint for the train cars, called a "Node." This blueprint tells us that each car will have a place for a number, a handle to the front car, and a handle to the back car.
   
   - Then, we make an empty train, called a "DoublyLinkedList." This train doesn't have any cars yet, so its front and back handles are empty.

 2. Adding Cars: 
   -  To add a car to the front: 
      - We build a new car with the number we want to add.
      - If the train is empty, this new car becomes both the front and back of the train.
      - If the train already has cars, we link the new car's front handle to the current front car, and we set the current front car's back handle to the new car. Then, we make the new car the front of the train.
  
    -  To add a car to the back:
      - We build a new car with the number we want to add.
      - If the train is empty, this new car becomes both the front and back of the train (just like adding to the front).
      - If the train already has cars, we link the current back car's front handle to the new car, and we set the new car's back handle to the current back car. Then, we make the new car the back of the train.
   
   -  To add a car in the middle: 
      - We build a new car with the number we want to add.
      - We find the car that's currently in the position where we want to add the new car.
      - We link the handles of the new car to the cars around it, so it gets connected in the right spot.

 3. Reading the Cars: 
   -  To read the cars from front to back: 
      - We start at the front car and move through the train, reading the numbers in each car, until we reach the back.
   
   -  To read the cars from back to front: 
      - We start at the back car and move through the train in the opposite direction, reading the numbers in each car, until we reach the front.

 That's it! Now you can create your own number trains and add cars wherever you want! '''


# 1. Create a blueprint for the train cars (nodes)
class Node:
   def __init__(self, data):
       # Each car holds a number (data) and has handles to the next and previous cars
       self.data = data
       self.next = None  # Handle to the car in front
       self.prev = None  # Handle to the car behind

# 2. Create an empty train (doubly linked list)
class DoublyLinkedList:
   def __init__(self):
       # The train starts empty with no cars
       self.head = None  # Handle to the front car
       self.tail = None  # Handle to the back car

   # 3. Add a car to the beginning of the train
   def insert_at_beginning(self, data):
       # Build a new car with the given number
       new_node = Node(data)

       # If the train is empty, the new car becomes both the front and back
       if self.head is None:
           self.head = self.tail = new_node
       else:
           # Link the new car's front handle to the current front car
           new_node.next = self.head
           # Link the current front car's back handle to the new car
           self.head.prev = new_node
           # Make the new car the front of the train
           self.head = new_node

   # 4. Add a car to the end of the train
   def insert_at_end(self, data):
       # Build a new car with the given number
       new_node = Node(data)

       # If the train is empty, the new car becomes both the front and back
       if self.tail is None:
           self.head = self.tail = new_node
       else:
           # Link the current back car's front handle to the new car
           self.tail.next = new_node
           # Link the new car's back handle to the current back car
           new_node.prev = self.tail
           # Make the new car the back of the train
           self.tail = new_node

   # 5. Add a car at a specific position in the train
   def insert_at_position(self, data, position):
       # Check for invalid positions
       if position < 1:
           print("Invalid position")
           return

       # Build a new car with the given number
       new_node = Node(data)

       # If the position is 1, add the car to the beginning
       if position == 1:
           self.insert_at_beginning(data)
           return

       # Find the car at the specified position
       current = self.head
       current_position = 1

       while current is not None and current_position < position - 1:
           current = current.next
           current_position += 1

       # If we reached the end of the train before finding the position, it's invalid
       if current is None:
           print("Position exceeds list size")
           return

       # Link the new car's handles to the cars around it
       new_node.next = current.next
       current.next.prev = new_node
       current.next = new_node
       new_node.prev = current

   # 6. Read the cars from front to back
   def print_forward(self):
       # Start at the front car
       current = self.head

       # While there are cars, read their numbers
       while current is not None:
           print(current.data, end=" ")
           # Move to the next car
           current = current.next

       print()  # Print a newline at the end

   # 7. Read the cars from back to front
   def print_backward(self):
       # Start at the back car
       current = self.tail

       # While there are cars, read their numbers
       while current is not None:
           print(current.data, end=" ")
           # Move to the previous car
           current = current.prev

       print()  # Print a newline at the end


# Example usage
dll = DoublyLinkedList()
dll.insert_at_beginning(5)
dll.insert_at_end(10)
dll.insert_at_position(8, 2)

print("Forward traversal:")
dll.print_forward()  # Output: 8 5 10

print("Backward traversal:")
dll.print_backward()  # Output: 10 5 8
