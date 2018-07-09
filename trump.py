# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 17:36:40 2018

@author: buryu-
"""
import random

class Trump:
    def __init__(self,jorker):
        self.jorker = jorker
        suit=['heart','diam','spade','club']
        if self.jorker==False:
            self.deck=list(range(13*4))
            for mark in range(4):
                for i in range(13):
                    self.deck[mark*13+i]=[suit[mark],i+1]
            self.decknum=52
        else:
            self.deck=list(range(13*4+2))
            for mark in range(4):
                for i in range(13):
                    self.deck[mark*13+i]=[suit[mark],i+1]
            self.deck[-1]=[5,14]
            self.deck[-2]=[5,14]
            self.decknum=54
        
            
    def draw(self,number):
        if number>self.decknum:
            print('too many number of card is drawed')
        else:
            output=list(range(number))
            for i in range(number):
                ind=random.randrange(self.decknum)
                output[i]=self.deck[ind]
                self.decknum=self.decknum-1
                del self.deck[ind]
        
        return output
    
    def shuffle(self):
        if self.jorker==False:
            self.deck=list(range(13*4))
            for mark in range(4):
                for i in range(13):
                    self.deck[mark*13+i]=[mark+1,i+1]
            self.decknum=52
        else:
            self.deck=list(range(13*4+2))
            for mark in range(4):
                for i in range(13):
                    self.deck[mark*13+i]=[mark+1,i+1]
            self.deck[-1]=[5,14]
            self.deck[-2]=[5,14]
            self.decknum=54
    
    
    
    
                