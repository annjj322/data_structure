class Node:
    """class node for linked list"""

    def __init__(self, item = None, link = None): # class에서 객체가 선언되면 자동으로 실행되는 method
        self.item = item
        self.link = link



class LinkedList:
    """class node for linked list"""

    def __init__(self): # class에서 객체가 선언되면 자동으로 실행되는 method
        self.root = None

    def append(self, item): # method
        newNode = Node(item)
        if self.root == None:
            self.root = newNode
        else:
            curNode = self.root
            while curNode.link != None:
                curNode = curNode.link # curNode의 link로 가면 주소상으로 다음 Node로 이동하게 되고, 이를 반복하면 None에 도달할 때 까지 이동하게 된다.
            curNode.link = newNode # None인 node의 link에 넣어준다.

    def pprint(self):
        curNode = self.root
        print(curNode.item,end=' ')
        while curNode.link != None:
            curNode = curNode.link
            print(curNode.item,end=' ')
        print()

    def insert(self, k, item):
        newNode = Node(item)
        curNode = self.root
        if k == 0:
            kNode = self.root
            self.root = newNode
            newNode.link = kNode
        elif k > 0:
            for _ in range(k-1):
                curNode = curNode.link # update code
                kNode = curNode.link
                curNode.link = newNode
                newNode.link = kNode
    
    def search(self, item):
        idx = 0
        curNode = self.root
        while curNode.item != item:
            idx += 1
            curNode = curNode.link
        return idx

    def delete(self, item):
        idx = self.search(item)
        if idx == 0:
            self.root = self.root.link
        elif idx > 0:
            curNode = self.root
            for _ in range(idx-1):
                curNode = curNode.link
            curNode.link = curNode.link.link


    def size(self):
        cnt = 0
        curNode = self.root
        while curNode != None:
            curNode = curNode.link
            cnt += 1
        print(cnt)


######################## concept #########################
# a.link = b
# b.link = c
# c.link = d
# d.link = None -> default value
##########################################################

if __name__ == '__main__':
    fruits = LinkedList()
    fruits.append('apple')
    fruits.append('pear')
    fruits.append('cherry')
    fruits.append('peach')
    fruits.search('cherry')
    fruits.insert(2,'potato')
    fruits.pprint()
    fruits.delete('potato')
    fruits.pprint()
    fruits.size()
