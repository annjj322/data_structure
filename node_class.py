class Node:
    """class node for linked list"""

    def __init__(self, item = None, link = None): # class에서 객체가 선언되면 자동으로 실행되는 method
        self.item = item
        self.link = link
        

a = Node('사과') # '사과' -> item
b = Node('앵두')
c = Node('배')
d = Node('포도')

######################## concept #########################
# a.link = b
# b.link = c
# c.link = d
# d.link = None -> default value
##########################################################

if __name__ == '__main__':
    print(a.item)
    print(a.link)