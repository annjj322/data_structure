from CBA2 import LinkedList



class Poly3:
    def __init__(self,maxOrder): # coefficient, order
        self.linked_list = LinkedList()
        self.maxOrder = maxOrder
    def setCoef(self,coef):
        self.linked_list.append(coef)
    def getCoef(self,order):
        curNode = self.linked_list.root
        for i in range(order):
            curNode = curNode.link
        if curNode.item[1] == order:
            return curNode.item[0]
        else:
            return 0

    @classmethod
    def add(cls,poly1,poly2): # linkedList type -> self.root부터 시작해서 더하기
        maxOrder = max(poly1.maxOrder, poly2.maxOrder)
        poly3 = Poly3(maxOrder)
         



if __name__ == '__main__':
    third_order = Poly3(3)
    forth_order = Poly3(4)

    third_order.setCoef((1,0))
    third_order.setCoef((2,1))
    third_order.setCoef((3,2))
    third_order.linked_list.pprint()

    forth_order.setCoef((2,0))
    forth_order.setCoef((1,1))
    forth_order.setCoef((5,2))
    forth_order.setCoef((4,3))
    forth_order.linked_list.pprint()
    print(third_order.linked_list.root.link.item)