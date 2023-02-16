### Stack
A stack is a data structure that represents a collection of elements in which the elements are inserted and removed from the same end. It follows the LIFO (Last-In-First-Out) principle, which means that the last element added to the stack will be the first one to be removed.

A stack can be implemented using an array or a linked list. The two main operations that can be performed on a stack are:

- Push: This operation adds an element to the top of the stack.

- Pop: This operation removes an element from the top of the stack.

```python
def stack():
    #initializing the stack
    stack = []
    return stack

def check_empty(stack):
    #checking if the stack is empty
    if len(stack)==0:
        return True
    else:
        return False
def push(stack,item):
    stack.append(item)
    # adding the item to the end of the stack
    print("item pushed is: "+item)

def pop(stack):
    if (check_empty(stack)):
        return "the stack is empty"
    #else remove the last element
    return stack.pop() # and return the element
def print_stack(stack):
    print(*stack)


s = stack()
push(s, str(1))
push(s, str(2))
push(s, str(3))
push(s,str(4))
pop(s)
print_stack(s)
push(s, str(5))
print_stack(s)
```
