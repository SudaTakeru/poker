# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 17:24:41 2018

@author: buryu-
"""
import trump
import Porker

class dealer:
    def __init__(self,n,coin):
        # n = number of player
        # minimum coin
        self.a=trump.Trump(0)
        self.b=Porker.Porker()
        self.n=n
        self.flag=0
        self.battle=list((1) for i in range(self.n) )
        self.battle2=list((0) for i in range(self.n) )
        self.betcoin=list((coin) for i in range(self.n) )
        
        
    def leaveplayer(self):
        if self.flag==0:
            if sum(self.battle)==1:
                win0=self.battle.index(max(self.battle))
                win=[win0]
            else:
                win=[i for i, x in enumerate(self.battle) if x == max(self.battle)]
        else:
            win=[100000000000]
        return win
        
    def ask(self,k):
        # for player k
        if self.battle[k]==1:
            print("Player "+str(k))
            
            act = input("Call or Raise or Drop?" + " [Call:1],[Raise:2],[Drop:0] ")
            act = int(act)
            if act==1:
                self.Bet(k)
            elif act==2:
                act = input("Raise: How?" + " $... ")
                act = int(act)
                self.Raise(k,act)
            else:
                self.Drop(k)
                
    def check_fininsh(self):
        self.flag=1 
        temp=list((1) for i in range(self.n) )
        for i in range(self.n):
            if self.battle[i]==0:
                temp[i]=0
        if sum(self.battle)==1 or self.battle2==temp:
            self.flag=0               
        return self.flag
    
    def Bet(self,k):
        self.battle[k]=1
        self.betcoin[k]=max(self.betcoin)
        self.battle2[k]=1
        
    def Call(self,k):
        self.battle[k]=1
        self.betcoin[k]=max(self.betcoin)
        self.battle2[k]=1

    def Raise(self,k,p):
        self.battle[k]=1
        self.battle2[k]=0
        if max(self.betcoin)<p:
            self.betcoin[k]=p

    def Drop(self,k):
        self.battle[k]=0
        self.battle2[k]=0
    
    def Draw(self,n,x,y):
        # n枚数、ｘ手札、ｙ捨て札のindex
        newcard=self.a.draw(n)
        del x[y]
        x.append(newcard)
        return x
    
    def check(self,k):
        self.battle[k]=1
    
    
    