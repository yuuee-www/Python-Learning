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
        if theHeight < 2 :
            self._height = 2
        elif theHeight > Pyramid.MAX_HEIGHT :
            self._height = Pyramid.MAX_HEIGHT
        else :
            self._height = theHeight
        
        if len(theSymbol.strip()) == 0 :         # the symbol is blank
            self._symbol = Pyramid.DEFAULT_SYMBOL
        else :
            self._symbol = theSymbol.strip()[0]


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
    