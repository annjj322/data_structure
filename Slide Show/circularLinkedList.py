import copy

class Node:
    def __init__(self, item=None, link=None) -> None:
        self.item = item
        self.link = link


class CircularLinkedList:
    def __init__(self):
        self.root = Node()
    
    def append(self, item):
        newItem = Node(item)
        curNode = self.root
        if curNode.link == None:
            curNode.link = newItem
        elif self.size() != 1:
            curNode = curNode.link
            while curNode.link != self.root.link:
                curNode = curNode.link
            curNode.link = newItem
        curNode = curNode.link
        curNode.link = self.root.link

    def pprint(self):
        curNode = self.root
        if curNode.link == None:
            print('there\'s no item')
        else:
            while curNode.link != None:    
                print(curNode.link.item,end=' ')
                curNode = curNode.link
            print('')

    def insert(self,k,item):
        curNode = self.root
        idx = self.search(item)
        for _ in range(idx-1):
            curNode = curNode.link
        

    def search(self,item):
        curNode = self.root
        idx = 0
        while curNode.item != item:
            idx+=1
            curNode = curNode.link
        if __name__ == '__main__':
            print(f'{item} is in index number {idx}') # python number x
        return idx

    def delete(self,item):
        curNode = self.root
        idx = self.search(item)
        for _ in range(idx-1):
            curNode = curNode.link
        curNode.link = curNode.link.link

    def size(self):
        curNode = self.root
        count = 0
        while curNode.link != self.root.link:
            count+=1
            curNode = curNode.link
        if __name__ == "__main__":
            print(count)

    

if __name__ == '__main__':
    fruits = CircularLinkedList()
    # fruits.pprint()
    fruits.append('사과')
    fruits.append('딸기')
    fruits.append('배')
    fruits.append('오렌지')
    fruits.append('포도')
    fruits.append('수박')
    fruits.append('블루베리')
    fruits.append('레몬')
    fruits.append('자두')
    fruits.delete('딸기')
    fruits.search('사과')
    fruits.pprint()
    fruits.size()