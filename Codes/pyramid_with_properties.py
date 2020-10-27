###  This module defines a class that models a pyramid printed from an ascii
#    character.
#

## A pyramid has a height and a symbol. An ascii representation of the pyramid
#  is returned by the __str__ method.
#

class Pyramid :

    MARGIN = 10 * ' '
    MAX_HEIGHT = 20
    DEFAULT_SYMBOL = '*'
        
    ## Constructs a pyramid with a given height from a given symbol.
    #  @param theHeight the height of the pyramid (default = 2)
    def __init__(self, theHeight = 2, theSymbol = '*') :
        self.height = theHeight
        self.symbol = theSymbol

    ## The height property allows get/set access to the Pyramid's height value.
    # 
    # The height must be between 2 and MAX_HEIGHT inclusive.
    # If the value is < 2, height is set to 2.
    # If the value > MAX_HEIGHT, height is set to MAX_HEIGHT
    @property
    def height(self):
        return self._height


    ## Sets the height attribute.
    #  @param value the height of the pyramid (default = 2)        
    @height.setter
    def height(self, value):
        if value < 2 :
            self._height = 2
        elif value > Pyramid.MAX_HEIGHT :
            self._height = Pyramid.MAX_HEIGHT
        else :
            self._height = value

    ## The symbol property allows get/set access to the Pyramid's symbol value.
    # 
    # If the symbol is blank, it is set to the DEFAULT_SYMBOL
    # 
    @property
    def symbol(self):
        return self._symbol


    ## Sets the symbol attribute.
    #  @param value the symbol        
    @symbol.setter
    def symbol(self, value):
        if len(value.strip()) == 0 :         # the symbol is blank
            self._symbol = Pyramid.DEFAULT_SYMBOL
        else :
            self._symbol = value.strip()[0]


    ## Builds the spaces for a line
    # @param currentLine the current line being printed.
    # @returns a string containing the spaces for a line.    
    def spacesForPyramidLine(self, currentLine) :
        spacesForPyramidLine = ""
        spacesForPyramidLine = Pyramid.MARGIN + (self._height + 1 - currentLine) * ' '
        return spacesForPyramidLine

 
    ## Builds the symbols for a line
    # @param currentLine the current line being printed.
    # @returns a string containing the symbols for a line.    
    def symbolsForPyramidLine(self, currentLine) :
        lineSymbols = self._symbol * ((currentLine * 2) - 1)
        return lineSymbols
 
 
    ## Builds a line of the pyramid
    # @returns a string containing the current line of the pyramid.    
    def pyramidLine(self, currentLine) :
        pyramidLine = self.spacesForPyramidLine(currentLine) + self.symbolsForPyramidLine(currentLine) + "\n" 
        return pyramidLine

        
    ## Builds the pyramid line by line and returns an ascii representation.
    # @returns pyramidString an ascii representation of the pyramid.
    def __str__(self) :
        pyramidString = ""
        for i in range(1, self._height + 1) :
            pyramidString = pyramidString + self.pyramidLine(i)
        return pyramidString
    