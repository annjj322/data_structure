import numpy as np
import copy

class SparseMatrix:
    def __init__(self,m,n) -> None:
        self.sList = [[m,n,0]]

    def append(self, i, j, val):
        self.sList.append([i,j,val])
        self.sList[0][2] += 1

    def shape(self):
        return (self.sList[0][0],self.sList[0][1])

    def pprint(self):
        x = np.zeros(self.shape())
        for i in range(1,len(self.sList)):
            x[self.sList[i][0], self.sList[i][1]] = self.sList[i][2]
        print(x)

    def getValue(self, m, n):
        for i in range(1, len(self.sList)):
            if self.sList[i][0] == m and self.sList[i][1] == n:
                return self.sList[i][2]
        return 0

    @classmethod
    def transpose(cls, x):
        sTrans = SparseMatrix(x.shape()[0],x.shape()[1])
        cls.transMatrix = copy.deepcopy(x.sList)
        for matValue in cls.transMatrix:
            matValue[0], matValue[1] = matValue[1], matValue[0]
        sTrans.sList = cls.transMatrix
        return sTrans
    
    # @classmethod
    # def add(cls, sparse1, sparse2): # n x n 번의 loop를 돌아야되는 문제가 있음.
    #     (m,n) = sparse1.shape()
    #     sparse3 = SparseMatrix(m,n)
    #     for i in range(m):
    #         for j in range(n):
    #             addValue = sparse1.getValue(i,j) + sparse2.getValue(i,j)
    #             if addValue != 0:
    #                 sparse3.append(i,j,addValue)
    #     return sparse3

    @classmethod
    def add(cls, sparse1, sparse2):  # sparse1 and sparse2 valid index -> add
        (m,n) = sparse1.shape()
        sparse3 = SparseMatrix(m,n)
        locations = set()
        for i in range(1,len(sparse1.sList)):
            locations.add((sparse1.sList[i][0],sparse1.sList[i][1]))
        for i in range(1,len(sparse2.sList)):
            locations.add((sparse2.sList[i][0],sparse2.sList[i][1]))
        # print(locations)
        for loc in locations:
            addValue = sparse1.getValue(loc[0],loc[1]) + sparse2.getValue(loc[0],loc[1])
            if addValue != 0:
                sparse3.append(loc[0],loc[1],addValue)
        return sparse3


if __name__ == '__main__':
    sMatrix1 = SparseMatrix(3,4)
    sMatrix1.append(0,0,1)
    sMatrix1.append(1,1,2)
    sMatrix1.append(1,3,3)
    sMatrix1.append(2,2,4)

    sMatrix2 = SparseMatrix(3,4)
    sMatrix2.append(0,0,3)
    sMatrix2.append(2,1,1)
    sMatrix2.append(1,2,8)
    sMatrix2.append(2,3,2)

    sMatrix1.pprint()
    sMatrix2.pprint()
    # sTrans = SparseMatrix.transpose(sMatrix1)
    # sTrans.pprint()
    sAdd = SparseMatrix.add(sMatrix1,sMatrix2)
    sAdd.pprint()