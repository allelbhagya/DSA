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
