
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
