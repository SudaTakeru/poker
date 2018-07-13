# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 18:06:58 2018

@author: buryu-
"""

class Porker:
    def __init__(self):
        self.p=0
        
        
    def judge(self,a):
        #a=list(ai)
        #ai=[result,strength,num] (return:hand,i)
        strength=list(range(len(a)))
        for i in range(len(a)):
            strength[i]=a[i][1]
        ind=max(strength)
        count=0
        ind2=[]
        for i in range(len(a)):
            if ind==strength[i]:
                count=count+1
                ind2.append(i)
        if count>1:
            s = a[ind2[0]][1]
            if s>6 or s==5 or s==4 or s==2:
                k=list(range(len(ind2)))
                for i in range(len(ind2)):
                    k[i]=a[ind2[i]][2]
                ind30=[i for i, x in enumerate(k) if x == max(k)]
                ind3=[]
                for i in range(len(ind30)):
                    ind3.append(ind2[ind30[i]])
            elif s==3:
                k=list(range(len(ind2)))
                for i in range(len(ind2)):
                    k[i]=max(a[ind2[i]][2])
                ind30=[i for i, x in enumerate(k) if x == max(k)]
                if len(ind30)==1:
                    ind3=ind2[ind30[0]]
                else:
                    for i in range(len(ind30)):
                        if type(a[ind30[i]][2])==int:
                            k[i]=a[ind30[i]][2]
                        else:
                            k[i]=min(a[ind30[i]][2])
                    ind30=[i for i, x in enumerate(k) if x == max(k)]
                    ind3=[]
                    for i in range(len(ind30)):
                        ind3.append(ind2[ind30[i]])
            else:
                ind3=ind2    
        else:
            ind3=ind2[0]
        return ind3
        
    def hand(self,x):
        [res,num]=self.straightflash(x)
        strength=9
        if res==True:
            result='straightflash'
        else:
            strength=strength-1
            [res,num]=self.fourcard(x)
            if res==True:
                result='fourcard'
            else:
                strength=strength-1
                [res,num]=self.fullhouse(x)
                if res==True:
                    result='fullhouse'
                else:
                    strength=strength-1
                    [res,num]=self.flash(x)
                    if res==True:
                        result='flash'
                    else:
                        strength=strength-1
                        [res,num]=self.straight(x)
                        if res==True:
                            result='straight'
                        else:
                            strength=strength-1
                            [res,num]=self.Threecard(x)
                            if res==True:
                                result='Threecard'
                            else:
                                strength=strength-1
                                [res,num]=self.TwoPair(x)
                                if res==True:
                                    result='TwoPair'
                                else:
                                    strength=strength-1
                                    [res,num]=self.Pair(x)
                                    if res==True:
                                        result='Pair'
                                    else:
                                        strength=strength-1
                                        result='garbage'
                                        num=list(range(len(x)))
                                        for i in range(len(x)):
                                            num[i]=x[i][1]
                                        num.sort()
        return [result,strength,num]
    
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
        number=list((0,0))
        k=0
        for i in range(len(x)-1):
            temp=x[i][1]
            cards=x
            
            count=0
            for ii in range(len(cards)):
                if temp==cards[ii][1]:
                    count=count+1
                if count==2:
                    if (k==0) or ((not temp == number[0]) and k==1):
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
    
    