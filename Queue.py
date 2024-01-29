class Queue: 
    def __init__(self): 
        self.items = [] 
 
    def is_empty(self): 
        return len(self.items) == 0 
 
    def enqueue(self, item): 
        self.items.append(item) 
 
    def dequeue(self): 
        if not self.is_empty(): 
            return self.items.pop(0) 
        else: 
            raise IndexError("Cannot dequeue from an empty queue") 
 
    def size(self): 
        return len(self.items) 
 
queue = Queue() 
 
queue.enqueue(1) 
queue.enqueue(2) 
queue.enqueue(3) 
 
print(queue.dequeue())   
print(queue.dequeue())   
 
print(queue.is_empty())   
 
 
print(queue.size()) 