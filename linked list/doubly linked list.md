# Doubly Linked List

A doubly linked list is a linear data structure that consists of a sequence of nodes, where each node stores an element and two references, one to the previous node and one to the next node in the sequence. The first node in the sequence is called the head of the list, and the last node is called the tail.

The main advantage of a doubly linked list is that it allows for more efficient insertion and deletion of nodes in the list, especially when compared to a singly linked list.

Operations performed:

- Insertion: Adding a new node at the beginning, end, or middle of the list.

- Deletion: Removing a node from the list.

- Traversal: Visiting each node in the list in order.

- Searching: Finding a node with a specific value.

```python
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.start = None
        self.last = None

    def append(self,data):
        #if DLL is empty then last Node is None
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            new_node = Node(data) #create new node
            self.last.next = new_node #next of last node as new node
            new_node.prev = self.last #previous of new node as last node
            new_node.next = None # no node after new one
            self.last = new_node #last node will be new node now

    def display(self,Type):
        if Type == 'left_to_right':
            current = self.head
            while current is not None:
                print(current.data, end = '<->')
                current= current.next
            print()
        else:
            current = self.last
            while current is not None:
                print(current.data, end = '<->')
                current = current.prev
            print()


dll = DLL()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.display('left_to_right')
dll.display('right_to_left')
```
