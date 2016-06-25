#! /usr/bin/env python
# -*- coding: utf-8 -*-
#生存:1,死亡0

class Lifegame():
    def __init__(self,n):
        self.field = [[0 for i in range(n)] for j in range(n)]
    
    def forward(self):
        self.nextField = [[0 for i in range(len(self.field))] for j in range(len(self.field))]
        for a in range(len(self.field)):
            for b in range(len(self.field)):
                self.checkCell(a,b)
        self.updateField()
    
    #生存数を教えてくれるやつ
    def countSurvivor(self,i,j): 
        count = 0
        for a in range(-1,2):
            for b in range(-1,2):
                if (i + a > 0 and j + b > 0 and i + a < len(self.field) and j + b < len(self.field)): 
                    if (self.field[i+a][j+b] == 1 and ((a != 0) or (b != 0))):
                        count += 1
        return count

    #cellに対して生存死亡判定をしてくれるやつ
    def checkCell(self,i,j): 
        tmp = self.countSurvivor(i,j)
        if tmp == 3:
            self.nextField[i][j] = 1
        elif tmp >= 4 or tmp <= 1:
            self.nextField[i][j] = 0
        else:
            self.nextField[i][j] = self.field[i][j]
    
    def updateField(self):
        self.field = self.nextField
    
    def printField(self):
        for a in range(len(self.field)):
            print(self.field[a])

