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




##### Poly1, Poly2 #####
class Poly1:
    def __init__(self, maxOrder): # append를 사용하지 x. 크기를 미리 정해뒀기 때문에 append를 사용하는 방식이 아님
        self.maxOrder = maxOrder
        self.coef = [0]*(self.maxOrder+1)

    def setCoef(self, coef, order):
        self.coef[order] = coef # order 자리에 coef를 넣어라

    def getCoef(self, order):
        if order > self.maxOrder:
            return 0
        else:
            return self.coef[order]

    @classmethod
    def add(cls, p, q):
        maxOrder = max(p.maxOrder, q.maxOrder)
        r = Poly1(maxOrder)
        for i in range(maxOrder+1):
            rCoef = p.getCoef(i) + q.getCoef(i)
            r.setCoef(rCoef,i)
        return r
    

class Poly2:
    def __init__(self,maxOrder):
        self.maxOrder = maxOrder
        self.coef = []
    def setCoef(self, coef):
        self.coef.append(coef)

    def getCoef(self, order):
        if order > self.maxOrder:
            return 0
        else:
            for i in range(len(self.coef)):
                if self.coef[i][1] == order:
                    return self.coef[i][0]
            return 0 # for loop를 다 돌아도 order 상에서 None으로 정의된 항들이 있기 때문에 0을 return 해주는 것.

    @classmethod
    def add(cls,p,q):
        maxOrder = max(p.maxOrder, q.maxOrder)
        r = Poly2(maxOrder)
        for i in range(maxOrder+1):
            r.setCoef((p.getCoef(i)+q.getCoef(i),i)) # setting self
        return r