import numpy as np
np.random.seed(seed = 1)
cookTime = np.random.normal(1,0.2,10)
cookTime = np.where(cookTime<0,0,cookTime)
print(cookTime)

class Queue:
    def __init__(self) -> None:
        self.q = []
    
    def enQueue(self,item):
        self.q.append(item)
    
    def isEmpty(self):
        return len(self.q) == 0
    
    def deQueue(self):
        if self.isEmpty() == False:
            return self.q.pop()
        else:
            return None
        
    def peek(self):
        return self.q[0]
    