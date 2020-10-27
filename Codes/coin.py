### This module defines a class that represents a coin
#

## A Coin has a face. 
#

import random

class Coin:
    
    # Static constants
    HEADS = 0
    TAILS = 1
    
    # Static variables
    headsSoFar = 0
    tailsSoFar = 0

    ## Constructor initializes the state of new Coin objects.
    def __init__(self):
        # set the attributes (the state in each Coin object)
        self.flip()


    ## Set the face of the coin to either heads or tails.
    #
    def flip(self):
        self._face = random.randint(0,1)
        if self._face == Coin.HEADS:
            Coin.headsSoFar += 1
        else:
            Coin.tailsSoFar += 1


    ## Return the number of heads flipped so far.
    # @return the number of heads so far
    def get_heads_so_far():
        return Coin.headsSoFar

    ## Return the number of tails flipped so far.
    # @return the number of tails so far    
    def get_tails_so_far():
        return Coin.tailsSoFar
       
    ## Return a string representation of a coin
    # @return a string representing the coin
    def __str__(self):
        if self._face == Coin.HEADS:
            the_face = "H"
        if self._face == Coin.TAILS:
            the_face = "T"
        return the_face
