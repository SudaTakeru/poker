# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 17:24:41 2018

@author: buryu-
"""
import trump
import Porker

class dealer:
    def __init__(self,n):
        # n = number of player
        self.a=trump.Trump(0)
        self.b=Porker.Porker()
        self.n=n
        self.battle=list((0) for i in range(self.n) )
        
    
    def ask(self,k):
        # for player k
        if not self.battle==list((0) for i in range(self.n) ):
            act = input("Call or Raise or Drop?" + " [Call:1],[Raise:2],[Drop:0] ")
            act = int(act)
                
        else:
            act = input("Bit or Pass?" + " [Bit:1],[Pass:0] ")
            act = int(act)
            if act==1:
                self.Bit(k)
            else:
                self.Drop(k)
    
    def Bit(self,k):
        self.battle[k]=1
    
    def Call(self,k):
        self.battle[k]=1
    
    def Raise(self,k,p):
        self.battle[k]=1

    def Drop(self,k):
        self.battle[k]=0
        
    
    def Draw(self,n,x,y):
        # n枚数、ｘ手札、ｙ捨て札のindex
        newcard=self.a.draw(n)
        del x[y]
        x.append(newcard)
        return x
    
    def check(self,k):
        self.battle[k]=1
    
    
    