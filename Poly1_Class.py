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
            


if __name__ == "__main__":
    p = Poly1(4)
    p.setCoef(3,0)
    p.setCoef(3,2)
    p.setCoef(4,4)

    q = Poly1(3)
    q.setCoef(1,0)
    q.setCoef(2,1)
    q.setCoef(3,3)
    q.setCoef(4,2)

    print(p.coef)
    print(q.coef)
    ans = Poly1.add(p,q).coef
    print(ans)