class Node:
    def __init__(self,item,link) -> None:
        self.item = item
        self.link = link

class CircleLinkedList:
    def __init__(self) -> None:
        self.root = None
        self.tail = None # circle linked list

    def append(self,item):
        newItem = Node(item)
        if self.root == None:
            self.root = newItem
        else:
            curNode = self.root
            while curNode.link == None:
                curNode = curNode.link
                curNode = newItem
    
    def size(self):
        curNode = self.root
        i = 1
        while curNode.link == None:
            i += 1
            curNode = curNode.link
    
    def search(self, item):
        pass