### Priority Queue

A priority queue is a data structure that allows for efficient insertion and retrieval of elements based on their priority. In a priority queue, each element is assigned a priority, and elements with higher priority are dequeued before elements with lower priority.

The basic operations supported by a priority queue are:

- Insert: Insert an element into the priority queue with a given priority.
- Extract: Remove and return the element with the highest priority from the queue.
- Peek: Return the element with the highest priority without removing it from the queue.

Applications: task scheduling, network routing, and computational geometry.

```python
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item, priority):
        #we have to maintain order in priority queue
        index = 0
        for i, j in self.queue:
            if priority < j:
                break
            index +=1

        self.queue.insert(index, (item, priority))
    
    def extract(self):
        if self.is_empty():
            return 'Queue is empty'
        #remove the item with highest priority 
        # that is the first element 
        return self.queue.pop()[0]
    
    def peek(self):
        # returning the element with highest priority
        #without removing the element
        return self.queue[-1][0]
    
    def is_empty(self):
        return len(self.queue) == 0


PQ = PriorityQueue()
PQ.insert(1,10)
PQ.insert(2,9)
PQ.insert(3,8)
print(PQ.extract())
print(PQ.extract())
print(PQ.extract())
print(PQ.extract())
```
