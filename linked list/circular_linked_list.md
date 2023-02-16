### Circular linked list

A circular linked list is a variation of the linked list data structure in which the last node in the list points back to the first node, forming a loop. This means that the next pointer of the last node in the list points to the first node in the list, rather than to NULL as in a regular linked list.

The main advantage of a circular linked list is that it allows for efficient traversal of the list, especially when we need to repeatedly iterate through the list. This is because, since the last node points back to the first node, we can traverse the list in a loop without the need to check for the end of the list.

Operations performed:

- Insertion: Adding a new node at the beginning, end, or middle of the list.

- Deletion: Removing a node from the list.

- Traversal: Visiting each node in the list in order.

- Searching: Finding a node with a specific value.

```python
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class CLL:
    def __init__(self):
        self.last = None

    def addEmpty(self,data):
        if self.last != None:
            return self.last #if not empty list, return last element
        new_node = Node(data) #new node create 
        self.last = new_node #last node of CLL is set as new node
        self.last.next = self.last #next of last node set as new node
        return self.last #only the new node will exist

    def addEnd(self,data):
        if self.last == None: #if list is empty create new node
            return self.addEmpty(data)
        new_node = Node(data)
        new_node.next = self.last.next #next of new node is next of last node
        self.last.next = new_node # next of last node is set as new node
        self.last = new_node #last node is now new node
        return self.last

    def transverse(self):
        current = self.last.next # will start traversing from last node
        while(current):
            print(current.data, end = ' ')
            current = current.next #keep moving on next node
            if current == self.last.next: #until we find the last node again
                break



c = CLL()
c.addEmpty(1)
c.addEnd(2)
c.addEnd(3)
c.addEnd(4)
c.transverse()
```
