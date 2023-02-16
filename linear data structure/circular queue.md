### Circular Queue Operations

two pointers: front and rear
- front : track the first element of the queue
- rear : track the last element of the queue
- initially front and rear = 0

1. Enqueue
   - checking if the queue is full
   - for first element = 0
   - increase index of rear
   - add new elements in position pointed by rear
2. Deuqeue
   - check if queue is empty 
   - return value pointed by front
   - increase front index by 1
  

```python
class CircularQueue():
    def __init__(self):
        self.queue = list()
        self.head = self.tail = 0
        self.length = 5
    
    def size(self): # calculating the total elements present in the list
        if self.tail >= self.head:
            return (self.tail - self.head)
        return (self.length - (self.head - self.tail))

    def enqueue(self,data):
        if self.size() == self.length - 1:
            return "Queue is full "
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.length
        return True
    
    def dequeue(self):
        if self.size() == 0:
            return "Queue is Empty"
        data = self.queue[self.head]
        self.head = (self.head + 1)% self.length
        return data

q = CircularQueue()
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
print(q.enqueue(4))
print(q.enqueue(5))
print(q.dequeue())
```
