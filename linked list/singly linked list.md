```python
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
  
class SLL:
    def __init__(self):
        self.head = None
    def push(self,new_data):
        new_node = Node(new_data)
  
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next =new_node
    def printSLL(self):
        temp = self.head
        while(temp):
            print(temp.data, end = ' ')
            temp = temp.next
    def delNode(self, key):
        temp = self.head
        if(temp is not None):
            if (temp.data == key):
                temp = None
                return
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if (temp is None):
            return
        prev.next = temp.next
        temp = None

  
s = SLL()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.printSLL()
print('\n')
s.delNode(4)
s.printSLL()
```
