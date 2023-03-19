from CBA2 import LinkedList



class Poly3:
    def __init__(self,maxOrder): # coefficient, order
        self.linked_list = LinkedList()
        self.maxOrder = maxOrder
    def setCoef(self,coef):
        self.linked_list.append(coef)
    def getCoef(self,order):
        curNode = self.linked_list.root # None 방지
        for i in range(order+1):
            if curNode.link is None:
                return 0
            elif curNode.link.item[1] == i:
                curNode = curNode.link
            else:
                pass # 비어있는 order은 i만 증가시키기.
        if curNode.item[1] != order:
            return 0
        else:
            return curNode.item[0]


    @classmethod
    def add(cls,poly1,poly2): # linkedList type -> self.root부터 시작해서 더하기
        maxOrder = max(poly1.maxOrder, poly2.maxOrder)
        poly3 = Poly3(maxOrder)
        for i in range(maxOrder):
            poly3.setCoef((poly1.getCoef(i)+poly2.getCoef(i),i))
        return poly3




if __name__ == '__main__':
    third_order = Poly3(3)
    forth_order = Poly3(4)

    third_order.setCoef((1,0))
    third_order.setCoef((2,1))
    third_order.setCoef((3,2))
    third_order.linked_list.pprint()

    forth_order.setCoef((2,0))
    forth_order.setCoef((5,2))
    forth_order.setCoef((4,3))
    forth_order.linked_list.pprint()

    result_function = Poly3.add(third_order,forth_order)
    result_function.linked_list.pprint()