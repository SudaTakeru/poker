# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 17:08:23 2018

@author: buryu-
"""

import trump
import Porker
import dealer

n=3
rate=10
deck=trump.Trump(0)
b=Porker.Porker()

field=deck.draw(5)
print(field)

player=list([] for i in range(n))
for i in range(n):
    player[i]=deck.draw(2)
    print('player '+str(i)+': '+str(player[i]))
deal=dealer.dealer(n,rate)
flag=1
while (flag):
    for i in range(n):
        deal.ask(i)
    flag=deal.check_fininsh()
    if not flag:
        break
    
leave=deal.leaveplayer()

if len(leave)>1:
    playerhandind=list(range(len(leave)))
    playerhand=list(range(len(leave)))
    for i in range(len(leave)):
        temphand=player[i]
        for ii in range(len(field)):
            temphand.append(field[ii])
        convs=deck.conbination(temphand,5)
        convhands=list([] for ii in range(len(convs)))
        for ii in range(len(convs)):
            convhands[ii]=b.hand(convs[ii])
        playerhandind[i]=b.judge(convhands)
        if not type(playerhandind[i])==int:
            playerhand[i]=convhands[playerhandind[i][0]]
        else:
            playerhand[i]=convhands[playerhandind[i]]
        
        print('player hand '+' of player'+str(leave[i])+' :'+str(playerhand[i]))
    win0=b.judge(playerhand)
    win=leave[win0]
else:
    win=leave[0]


print('Winner :'+str(win))


