import operator
def evaluate(parseTree):
    opers = {'+':operator.add,'-':operator.sub,\
             '*':oeprator.mul,'/':operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(lefC),evaluate(rightC))
    else:
        return parseTree.getRootVal()
    
