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

    def peek(self):
        return self.coef[0]
    
    def pop(self):
        return self.coef.pop(0)

    @classmethod
    def add(cls,p,q):
        maxOrder = max(p.maxOrder, q.maxOrder)
        r = Poly2(maxOrder)
        while len(p.coef) > 0 and len(q.coef) > 0:
            if p.peek()[1] > q.peek()[1]: # 남아있는 p의 coef를 pop 해야된다
                r.setCoef(p.pop()) # p.pop은 tuple
            elif p.peek()[1] == q.peek()[1]:
                _tmp1 = p.pop()
                _tmp2 = q.pop()
                r.setCoef((_tmp1[0]+_tmp2[0],_tmp1[1]))
            else:
                r.setCoef(q.pop())
        return r

if __name__ == "__main__":
    p = Poly2(4)
    p.setCoef((4,4))
    p.setCoef((3,2))
    p.setCoef((3,0))
    print(p.coef)

    q = Poly2(3)
    q.setCoef((3,3))
    q.setCoef((4,2))
    q.setCoef((2,1))
    q.setCoef((1,0))
    print(q.coef)

    r = Poly2.add(p,q)
    print(r.coef)