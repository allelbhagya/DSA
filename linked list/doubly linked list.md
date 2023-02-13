
```python
class Node:

    def __init__(self,data):

        self.previous=None

        self.data = data

        self.next = None

  

class DLL:

    def __init__(self):

        self.head = None

        self.start_node = None

        self.last_node = None

  

    def append(self,data):

        # if DLL is empty then last node is None

        if self.last_node is None:

            self.head = Node(data)

            self.last_node = self.head

        else: #adding node at tail

            new_node = Node(data)

            self.last_node.next = new_node

            new_node.previous = self.last_node

            new_node.next = None

            self.last_node=new_node

  

    def display(self,Type):

        if Type == 'Left_to_Right':

            current = self.head

            while current is not None:

                print(current.data,end='<->')

                current=current.next

            print()

        else:

            current=self.last_node

            while current is not None:

                print(current.data,end='<->')

                current=current.previous

            print()

  

if __name__=='__main__':

    dll = DLL()

    dll.append(1)

    dll.append(2)

    dll.append(3)

    dll.append(4)

    dll.display('Left_to_Right')

    dll.display('Right_to_Left')
```