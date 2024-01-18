# Question: 5.Write a Python function to search for a specific value in a circular linked list.

''' Here's a kid-friendly explanation of the code:  

  Imagine a train with special cars:  

- Each car holds a number (like a toy or a candy).
- The first car is the "head" car.
- The last car doesn't end the train; it's connected back to the head car, making a circle! This is our circular linked list.

  Our job is to find a specific toy or candy (the "value") in the train.  

  Here's how the code works:  

1.   Checking if the train is empty:  
   - If there are no cars (an empty train), we say "Nope, the toy isn't here!" and we're done.

2.   Starting the search:  
   - We hop into the head car to start looking.

3.   Going through each car:  
   - We check the toy or candy in the current car.
   - If it's the one we're looking for, we shout "Found it!" and stop searching.
   - If not, we move to the next car.

4.   Making sure we don't go in circles forever:  
   - If we reach the head car again without finding the toy, it means we've checked the whole train and it's not there. So we say "Nope, it's not in this train!"

  Key points to remember:  

- Each car is like a box that holds a value and a pointer to the next car.
- The circular linked list is like a train that loops back on itself.
- The search function goes through each car, checking for the value.
- It's important to handle the circularity to avoid getting stuck in an infinite loop.

  Think of it like a treasure hunt on a train! '''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def search(self, value):
        """Searches for a specific value in the circular linked list."""
        if self.head is None:
            return False  # Empty list

        curr = self.head
        while True:
            if curr.data == value:
                return True  # Value found

            # Move to the next node, handling circularity
            curr = curr.next
            if curr == self.head:
                break  # Traversed the entire list

        return False  # Value not found

# Example Usage

# Create a circular linked list
list = CircularLinkedList()
list.head = Node(10)
list.head.next = Node(20)
list.head.next.next = Node(30)
list.head.next.next.next = list.head  # Make it circular

# Search for a value
print(list.search(20))   # True
print(list.search(40))   # False