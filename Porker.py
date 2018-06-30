# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 18:06:58 2018

@author: buryu-
"""

class Porker:
    def __init__(self):
        self.p=0
        
    def hand(self,x):
        [res,num]=self.straightflash(x)
        if res==True:
            result='straightflash'
        else:
            [res,num]=self.fourcard(x)
            if res==True:
                result='fourcard'
            else:
                [res,num]=self.fullhouse(x)
                if res==True:
                    result='fullhouse'
                else:
                    [res,num]=self.flash(x)
                    if res==True:
                        result='flash'
                    else:
                        [res,num]=self.straight(x)
                        if res==True:
                            result='straight'
                        else:
                            [res,num]=self.Threecard(x)
                            if res==True:
                                result='Threecard'
                            else:
                                [res,num]=self.TwoPair(x)
                                if res==True:
                                    result='TwoPair'
                                else:
                                    [res,num]=self.Pair(x)
                                    if res==True:
                                        result='Pair'
                                    else:
                                        result='garbage'
                                        num=list(range(len(x)))
                                        for i in range(len(x)):
                                            num[i]=x[i][1]
        return [result,num]
    
    def straightflash(self,x):
        result=False
        [res1,num3]=self.flash(x)
        [res2,num]=self.straight(x)
        if res1==1 and res2==1:
            result=True
        return [result,num]
        
    def flash(self,x):
        result=False
        n=list(range(len(x)))
        nn=list(range(len(x)))
        flashcards=list(range(len(x)))
        
        for i in range(len(x)):
            n[i]=x[i][0]
            nn[i]=x[i][1]
            flashcards[i]=n[0]
        if flashcards==n:
            result=True
        nn.sort()
        return [result,nn]
        
    def straight(self,x):
        result=False
        n=list(range(len(x)))
        for i in range(len(x)):
            n[i]=x[i][1]
        n.sort()
        minn=n[0]
        if minn==1 and n[len(x)-1]==13:
            n[0]=14
            n.sort()
            minn=n[0]
        straightcards=list(range(len(x)))
        for i in range(len(x)):
            straightcards[i]=minn+i
        if straightcards==n:
            result=True
        return [result,minn]
        
    def fourcard(self,x):
        result=False
        number=[]
        for i in range(len(x)-1):
            temp=x[i][1]
            cards=x
            
            count=0
            for ii in range(len(cards)-1):
                if temp==cards[ii][1]:
                    count=count+1
                if count>=4:
                    result=True
                    number=temp
                    break
                
                    
        return [result,number]
    
    def fullhouse(self,x):
        result=False
        [res1,num3]=self.Threecard(x)
        [res2,num]=self.TwoPair(x)
        if res1==1 and res2==1:
            result=True
        
        return [result,num3]
        
        
    def Threecard(self,x):
        result=False
        number=[]
        for i in range(len(x)-1):
            temp=x[i][1]
            cards=x
            
            count=0
            for ii in range(len(cards)-1):
                if temp==cards[ii][1]:
                    count=count+1
                if count>=3:
                    number=temp
                    result=True
                    break
                
                
        return [result,number]

    def TwoPair(self,x):
        result=False
        number=list((0,0,0))
        k=0
        for i in range(len(x)-1):
            temp=x[i][1]
            cards=x
            
            count=0
            for ii in range(len(cards)):
                if temp==cards[ii][1]:
                    count=count+1
                if count==2:
                    if not temp == number[0]:
                        number[k]=temp
                        k=k+1
                        if k==2:
                            result=True
                        break
                
                
        return [result,number]
    
    def Pair(self,x):
        result=False
        number=[]
        for i in range(len(x)-1):
            temp=x[i][1]
            cards=x
            
            count=0
            for ii in range(len(cards)):
                if temp==cards[ii][1]:
                    count=count+1
                if count>=2:
                    number=temp
                    result=True
                    break
                
                
        return [result,number]
    
    