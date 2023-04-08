#%%

import numpy as np
import matplotlib.pyplot as plt



class Cust:
    def __init__(self, arriveT, orderT=None) -> None:
        self.cookT = 1.
        self.arriveT = arriveT
        if orderT == None:
            self.orderT = arriveT
        else:
            self.orderT = orderT
        
        self.outT = None

    def arriveTime(self):
        return self.arriveT
    
    # def orderTime(self): # cook time -> constant 라서 1단계에서는 의미가 없음
    #     pass 

    def outTime(self):
        self.outT = self.orderT + self.cookT
        return self.outT

class Shop:
    def __init__(self) -> None:
        self.custQueue = [] # 들어오는 모든 값들은 Cust 객체. 여기서 뽑아서 나가고 들어오는 값들을 getCust 하면 self.getCust().orderTime 처럼 사용가능?

    def getSize(self):
        return len(self.custQueue)
    
    def entCust(self,cust):
        self.custQueue.append(cust)

    def isEmpty(self):
        return len(self.custQueue) == 0

    
    def outCust(self, cust):

        if self.getCust().outTime() < cust.arriveT: # new Cust arrive time > old Cust out time -> old Cust OUT
            return self.custQueue.pop(0)
        else:
            pass


    def getCust(self):
        if self.isEmpty() == False:
            return self.custQueue[0]
        else:
            return None
    
    def getLast(self):
        if self.isEmpty() == False:
            return self.custQueue[-1]
        else:
            pass
        
def randNum(lamda):
    u = np.random.random(1)
    x = -lamda * np.log(u)
    return x[0]

def main():
    # 난수를 생성하고 현재시간을 0~60*14 만큼 늘려가면서 cust 생성
    
    
    # main loop
    curTime = 0
    i = 0
    coffeeShop = Shop() # shop 선언
    custList = []
    # randTime = x1 # 2번 추가문제 이전 내용

    while curTime < 14*60: # min
        if 5*60 < curTime < 6*60 :
            curTime += randNum(0.5)
        else:
            curTime += randNum(1)
        # if 5*60 < curTime < 6*60 :
        #     randTime = x2
        # else:
        #     randTime = x1
        try :
            preOut = coffeeShop.getLast().outT
            randCust = Cust(curTime,preOut) # pre cust out time
        except AttributeError:
            randCust = Cust(curTime)
        coffeeShop.entCust(randCust) # shop 입장
        
        # Cust OUT
        for j in range(coffeeShop.getSize()-1):    
            coffeeShop.outCust(randCust) # 일단 길이만큼 실행

        # Cust NUM
        custList.append(coffeeShop.getSize())
        i += 1
    print(custList)
    print(max(custList)) # Queue의 최대인원
    plt.figure(3)
    plt.plot(custList)
    plt.show()
        
if __name__ == '__main__':
    main()

# %%
