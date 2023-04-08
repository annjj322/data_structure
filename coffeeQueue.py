#%%

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(seed = 1)
u = np.random.random(1000)
lamda = 1
x = -lamda * np.log(u) # 난수



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
        

def main():
    # 난수를 생성하고 현재시간을 0~60*14 만큼 늘려가면서 cust 생성
    
    # main loop
    curTime = 0
    randTime = x
    i = 0
    coffeeShop = Shop() # shop 선언
    preCurTime = None
    custList = []
    while curTime < 14*60: # min
        curTime += randTime[i]
        try :
            randCust = Cust(curTime,preCurTime.orderT) # random num 숫자를 대입
        except AttributeError:
            randCust = Cust(curTime)
        coffeeShop.entCust(randCust) # shop 입장
        
        # Cust OUT
        for j in range(coffeeShop.getSize()):    
            coffeeShop.outCust(randCust) # 일단 길이만큼 실행
        
        # pre data
        preCurTime = curTime

        # Cust NUM
        custList.append(coffeeShop.getSize())
        i += 1
    print(custList)
    print(max(custList))
    plt.plot(custList)
    plt.show()
        
if __name__ == '__main__':
    main()

# %%
