"""
Linked List Insertion Operations
    1. Insertion at the beginning/head
    2. Insertion at the end/tail
    3. Insertion at a specific position
    4. Insertion at the middle
    5. Insertion after a given node
    6. Insertion before a given node
    7. Sorted Insertion
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertion_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        current_node = self.head

        while (current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    def insert_at_position(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0

        if index == 0:
            self.insertion_at_beginning(data)

        while current_node is not None and position+1!=index:
            position=position+1
            current_node=current_node.next

        new_node.next=current_node.next
        current_node.next=new_node

    def insert_at_middle(self,data):
        pass




    def print_LList(self):
        current_node = self.head

        while (current_node):
            print(current_node.data, end="->")
            current_node = current_node.next


newLL = LinkedList()
newLL.insertion_at_beginning(3)
newLL.insertion_at_beginning(4)
newLL.insert_at_end(13)
newLL.insert_at_end(21)
newLL.insert_at_end(23)
newLL.insert_at_end(27)
newLL.insert_at_position(17,1)
newLL.insert_at_middle(19)
newLL.print_LList()
