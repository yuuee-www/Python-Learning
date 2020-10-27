### This module defines a class that represents a british coin.
# BritishCoin inherits from the Coin class
#

## A british coin has a value. 
#
from coin import Coin 


class BritishCoin(Coin) :
    
    UNIT = "pence"
    ALLOWED_VALUES = {1 : "one", 2 : "two", 5 : "five", 10 : "ten", \
                     20 : "twenty", 50 : "fifty", 100 : "one hundred", 200 : "two hundred"}


    def __init__(self, theValue = 1) :
        super().__init__()
        self.value = theValue


    ## value property allows get/set access to BritishCoin's value.
    #  The value must be set to one of the permissable values in ALLOWED_VALUES.
    #  If the value passed to the setter is not in the list ALLOWED_VALUES then
    #  the value attribute will be set to the lowest coin value in the list.
    #
    @property
    def value(self):
        return self._value


    @value.setter
    def value(self, valueAmount) :
        if valueAmount in list(self.ALLOWED_VALUES) :
            self._value = valueAmount
        else :
            self._value = min(list(self.ALLOWED_VALUES))


    def __str__(self) :
        return "value: " +  self.ALLOWED_VALUES[self.value] + " " + self.UNIT \
               + " showing face: " + super().__str__()
        
    
    def __eq__(self, otherCoin) :
        if isinstance(otherCoin, BritishCoin) :
            return (self.sameFaceAs(otherCoin) and self.sameValueAs(otherCoin))
        else :
            raise TypeError("Both objects must have the same type.")

    
    def sameFaceAs(self, otherCoin) :
        return super().__eq__(otherCoin)    
    
    def sameValueAs(self, otherCoin) :
        return self.value == otherCoin.value
    
def main() :
    # a simple main function to test this class
    coin1 = BritishCoin()
    coin2 = BritishCoin(1)
    coin3 = BritishCoin(2)
    coin4 = BritishCoin(3)
    print("First coin: " + str(coin1))
    print("Second coin: " + str(coin2))
    print("Third coin: " + str(coin3))
    print("Fourth coin: " + str(coin4))
    print("The first two coins are ", end="")
    if coin1 != coin2 :
        print("not ", end="")
    print("equal.")

if __name__ == '__main__':
    main()