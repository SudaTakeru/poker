# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 12:53:53 2018

@author: buryu-
"""

import trump
import Porker

deck=trump.Trump(0)
b=Porker.Porker()

k=deck.draw(5)
#[re,st,num]
a=b.hand(k)
#print(str(re)+' '+str(num)+' '+str(st))
print(str(k)+'\n'+a[0]+' '+str(a[2]))

k2=deck.draw(5)
#[re2,st2,num2]
a2=b.hand(k2)
#print(str(re)+' '+str(num)+' '+str(st))
print(str(k2)+'\n'+a2[0]+' '+str(a2[2]))

c=b.judge([a,a2])
me=''
for i in range(len(c)):
    me=me+str(c[i])+ ' '
print('Win Player :'+me)    


deck=trump.Trump(0)
b=Porker.Porker()
playernum=2
    
    
    