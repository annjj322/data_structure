import copy

class Node:
    def __init__(self, item=None, link=None) -> None:
        self.item = item
        self.link = link


class LinkedList:
    def __init__(self):
        self.root = Node()
    
    def append(self, item):
        newItem = Node(item)
        curNode = self.root
        if curNode.link == None:
            curNode.link = newItem
        else:
            while curNode.link != None:
                curNode = curNode.link
            curNode.link = newItem

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
        while curNode.link != None:
            count+=1
            curNode = curNode.link
        print(count)

    def switch(self, item1, item2): # item1 = 
        item1_node_pre = self.root # self.root.item -> None
        item2_node_pre = self.root
        item1_idx = self.search(item1)
        item2_idx = self.search(item2)

        
        for i in range(item1_idx-1): # target node 의 1개 전까지 찾아주는 loop
            item1_node_pre = item1_node_pre.link
        for i in range(item2_idx-1):
            item2_node_pre = item2_node_pre.link
        
        if item1_idx > item2_idx:
            _tmp = item1_idx
            item1_idx = item2_idx
            item2_idx = _tmp # 작은 index를 item1로 변경
        
        # if item1_idx == 1:
        #     self.root.link = 

        ###### main switch #####
        item11_input = copy.deepcopy(item1_node_pre.link)
        item1_input = copy.deepcopy(item1_node_pre.link)

        item22_input = copy.deepcopy(item2_node_pre.link)
        item2_input = copy.deepcopy(item2_node_pre.link)


        item1_node_pre.link = item2_input # 2 -> 7 code
        item2_node_pre.link = item1_input # 6 -> 3 code

        item1_node_pre.link.link = item11_input.link # 7 -> 4 code

        item2_node_pre.link.link = item22_input.link # 3 -> 7 code

        item1_node_pre.link.link.link.link.link = item2_node_pre.link
### 질문 : 왜 item2 node의 6 -> 7 코드를 바꿔도 안바뀌는가?
### 다른 코드인가? deep copy를 사용해도 적용되지 않는가?

if __name__ == '__main__':
    fruits = LinkedList()
    # fruits.pprint()
    fruits.append('11')
    fruits.append('22')
    fruits.append('33')
    fruits.append('44')
    fruits.append('55')
    fruits.append('66')
    fruits.append('77')
    fruits.append('88')
    fruits.append('99')
    # fruits.pprint()
    fruits.switch('33','77')
    # fruits.size()
    fruits.pprint()
    # fruits.search('apple')
    # fruits.delete('cherry')
    # fruits.size()