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