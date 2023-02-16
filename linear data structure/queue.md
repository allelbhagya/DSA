### Queue 
A queue is a data structure that represents a collection of elements in which the elements are inserted from one end and removed from the other end. 
It follows the FIFO (First-In-First-Out) principle, which means that the first element added to the queue will be the first one to be removed.

The two main operations that can be performed on a queue are:

Enqueue: This operation adds an element to the end of the queue.

Dequeue: This operation removes an element from the front of the queue.

````python
class Queue:

    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue)<1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.display()
q.dequeue()
q.display()
```
