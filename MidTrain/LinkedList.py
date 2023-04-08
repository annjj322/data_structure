class Node:
    def __init__(self,item=None,link = None) -> None:
        self.link = link
        self.item = item

class LinkedList:
    def __init__(self) -> None:
        self.root = None # empty node
        
    def append(self, item):
        newNode = Node(item)
        if self.root == None:
            self.root = newNode
        else:
            curNode = self.root
            while curNode.link != None:
                curNode = curNode.link # final node
            curNode.link = newNode

    def size(self):
        curNode = self.root
        i = 1
        while curNode.link != None:
            i += 1
            curNode = curNode.link
        return i

    def pprint(self):
        curNode = self.root
        size = self.size()
        for i in range(size):
            print(curNode.item)
            curNode = curNode.link

    def search(self,item):
        i = 1
        curNode = self.root
        while curNode.item == item:
            curNode = curNode.link
            i += 1
        return i

    def delete(self,item):
        curNode = self.root
        ind = self.search(item)
        for _ in range(ind):
            curNode = curNode.link
        curNode.link = curNode.link.link

    def insert(self, k, item):
        newNode = Node(item)
        curNode = self.root
        if k == 1: 
            self.root = newNode
            self.root.link = curNode
        for _ in range(k-2):
            curNode = curNode.link
        newNode.link = curNode.link
        curNode.link = newNode

if __name__ == '__main__':
    test = LinkedList()
    test.append('hello')
    test.append('bye')
    test.append('you')
    test.append('me')
    test.append('I')
    test.delete('you') # delete Node
    test.insert(1,'HI!')
    test.pprint() # print all ## update insert