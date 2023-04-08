class Stack:
    def __init__(self):
        self.stackItem = []

    def push(self, item):
        self.stackItem.append(item)

    def pop(self):
        if self.isEmpty() == True:
            return None
        else:
            _tmp = self.stackItem[-1]
            self.stackItem = self.stackItem[:-1]
            return _tmp # return _tmp to use pop value
    
    def isEmpty(self):
        return len(self.stackItem) == 0 # == -> True , != -> False
    
    def delete(self):
        self.stackItem = self.stackItem[:-1]

    def peek(self):
        if self.isEmpty() == True:
            return None
        else:
            return self.stackItem[-1]
        
    def size(self):
        return len(self.stackItem)
    


class Calculator:
    def __init__(self) -> list:
        self.postStack = Stack()
        self.postList = []
        self.calcStack = Stack()

    def isOper(self,item):
        if item == '+' or item == '-' or item == '*' or item == '/':
            return True
        else:
            return False
        
    def isNum(self,item):
        try:
            float(item) # only num type can change into float type
            return True
        except ValueError:
            return False

    def postfixAgorithm(self, cal_obj):
        cal_obj = cal_obj.split(' ')
        print(cal_obj)
        for item in cal_obj:
            if item == '(':
                self.postStack.push(item)
            elif item == ')':
                while True:
                    __tmp = self.postStack.pop()
                    if __tmp != '(':
                        self.postList.append(__tmp)
                    else:
                        break
            elif item == '+' or item == '-':
                while self.isOper(self.postStack.peek()) == True:
                    self.postList.append(self.postStack.pop())
                self.postStack.push(item)
            elif item == '*' or item == '/':
                while self.postStack.peek() == '*' or self.postStack.peek() == '/':
                    self.postList.append(self.postStack.pop())
                self.postStack.push(item)
            elif self.isNum(item) == True:
                self.postList.append(item)
        print(self.postList)
        print(self.postStack.stackItem)

        while self.postStack.isEmpty() == False:
            self.postList.append(self.postStack.pop())
    
    def calculate(self):
        for item in self.postList:
            if self.isOper(item) == False:
                self.calcStack.push(item)
            else:
                _num1 = float(self.calcStack.pop())
                _num2 = float(self.calcStack.pop())
                if item == '+':
                    self.calcStack.push(_num2 + _num1)
                elif item == '-':
                    self.calcStack.push(_num2 - _num1)
                elif item == '*':
                    self.calcStack.push(_num2 * _num1)
                else:
                    self.calcStack.push(_num2 / _num1)
        return self.calcStack.pop()


if __name__ == '__main__':
    ans = Calculator()
    ans.postfixAgorithm('( 12.3 + 6 ) * 3 / 6 + 12 * ( 1 + 2 + 4 ) / 3')
    print(eval('( 12.3 + 6 ) * 3 / 6 + 12 * ( 1 + 2 + 4) / 3'))
    answer = ans.calculate()
    print(answer)