from CBA2 import LinkedList, Node



class Poly3:
    def __init__(self,maxOrder): # coefficient, order
        self.linked_list = LinkedList()
        self.maxOrder = maxOrder
    def setCoef(self,coef):
        self.linked_list.append(coef)
    def getCoef(self,order):
        pass

    @classmethod
    def add(cls,poly1,poly2): # linkedList type -> self.root부터 시작해서 더하기
        curNode_1 = poly1.linked_list.root
        curNode_2 = poly2.linked_list.root
         



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