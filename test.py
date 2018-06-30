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
[re,num]=b.hand(k)
print(str(re)+' '+str(num))
print(str(k))
