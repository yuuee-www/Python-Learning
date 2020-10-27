from pyramid_with_properties import Pyramid



pyr1 = Pyramid()

height = int(input("Enter the height of the pyramid: "))
symbol = input("Enter the symbol: ")                
pyr2 = Pyramid(height, symbol)

print(pyr1)
print(pyr2)