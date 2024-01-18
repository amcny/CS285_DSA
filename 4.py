# Question: 4. write a Python program that demonstrates the deletion of multiple nodes with different values from a circular linked list:

'''  Here's a kid-friendly explanation of the code:  

  Imagine a train with special cars that can loop back to the front!  

  Each car holds a number (like a toy or a snack), and the train can change which car is at the front.  

  1. Creating Train Cars:  

- We make a blueprint for a "car" called `Node`. Each car has two things:
    - A pocket to hold a number (`data`).
    - An arrow pointing to the next car (`next`).

  2. Building the Train:  

- We make a "train station" called `CircularLinkedList` to manage the cars.
- It starts empty, with no cars (`head = None`).

  3. Adding Cars to the Front:  

- When we want to add a new car (`push`), we:
    - Create a new car with the number we want to add.
    - Point its arrow to the current front car.
    - If there are already cars, we find the last car and make it point to the new car, creating the loop!
    - Make the new car the front car.

  4. Removing Cars:  

- When we want to remove a car (`deleteNode`), we:
    - Check if there are any cars at all. If not, we're done.
    - If there's only one car, we make the station empty.
    - Otherwise, we look for the car we want to remove:
        - If it's the front car, we find the last car and make it point to the next car after the front, becoming the new front.
        - If it's in the middle, we make the car before it point to the car after it, skipping over the one we want to remove.

  5. Showing the Train:  

- To see all the cars in the train (`printList`), we:
    - Start at the front car.
    - Print the number in each car.
    - Move to the next car.
    - Keep going until we're back at the front car.

  6. The Main Part:  

- We make a new train station (`cllist`).
- We add some cars with numbers (`20`, `4`, `15`, `10`).
- We print the train to see the original order.
- We remove two cars with numbers `4` and `15`.
- We print the train again to see the new order.

  That's how the code creates and manages this special loopy train with cars that hold numbers! '''


class Node:
   def __init__(self, data):
       self.data = data
       self.next = None

class CircularLinkedList:
   def __init__(self):
       self.head = None

   def push(self, new_data):
       new_node = Node(new_data)
       new_node.next = self.head
       if self.head is not None:
           last = self.head
           while last.next != self.head:
               last = last.next
           last.next = new_node
       else:
           new_node.next = new_node  # For only one node
       self.head = new_node

   def deleteNode(self, key):
       if self.head is None:
           return

       last = self.head
       if last.next == self.head and last.data == key:  # Only one node
           self.head = None
           return

       while last.next != self.head:
           if last.next.data == key:
               break
           last = last.next

       if last.next == self.head and last.next.data == key:  # Head node to be deleted
           last_node = self.head
           while last_node.next != self.head:
               last_node = last_node.next
           last_node.next = last_node.next.next
           self.head = last_node.next
       else:
           last.next = last.next.next

   def printList(self):
       temp = self.head
       if self.head is not None:
           while True:
               print(temp.data, end=" ")
               temp = temp.next
               if temp == self.head:
                   break
           print()

if __name__ == '__main__':
   cllist = CircularLinkedList()
   cllist.push(20)
   cllist.push(4)
   cllist.push(15)
   cllist.push(10)

   print("Original list:")
   cllist.printList()

   cllist.deleteNode(4)
   cllist.deleteNode(15)

   print("\nList after deleting 4 and 15:")
   cllist.printList()