class node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class linked_list:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self, data):
        newnode = node(data)
        