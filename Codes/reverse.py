def main():
   scores = readFloats(5)
   multiply(scores, 10)
   print("\nReversed numbers: ")
   printReversed(scores)

def readFloats(numberOfInputs):
   print("Enter", numberOfInputs, "numbers:")
   inputs = []
   for i in range(numberOfInputs):
      value = float(input(""))
      inputs.append(value)
      
   return inputs

def multiply(values, factor):
   for i in range(len(values)):
      values[i] = values[i] * factor

def printReversed(values):
   for value in reversed(values):
     print(value)
   
main()
