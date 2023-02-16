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
