def create_stack(max_capacity): 
    stack = [] 
    max_capacity = max(max_capacity, 0)  
    return stack, max_capacity 
 
 
def is_full(stack, max_capacity): 
    return len(stack) == max_capacity 
 
 
def is_empty(stack): 
    return len(stack) == 0 
 
 
def push(stack, item, max_capacity): 
    if is_full(stack, max_capacity): 
        print("Stack overflow. Cannot push item:", item) 
    else: 
        stack.append(item) 
        print("Pushed item:", item) 
 
 
def pop(stack): 
    if is_empty(stack): 
        return "Stack underflow" 
     
    return stack.pop() 
 
 
max_capacity = 3 
stack, max_capacity = create_stack(max_capacity) 
 
push(stack, 1, max_capacity) 
push(stack, 2, max_capacity) 
push(stack, 3, max_capacity) 
push(stack, 4, max_capacity)   
print("Popped item:", pop(stack)) 
print("Stack after popping an element:", stack) 
print("Popped item:", pop(stack)) 
print("Stack after popping an element:", stack) 
print("Popped item:", pop(stack)) 
print("Stack after popping an element:", stack) 
print("Popped item:", pop(stack)) 