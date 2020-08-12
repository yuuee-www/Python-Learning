def main():
  while True:
      try:
          binary_strings = input("Enter a comma separated list of binary numbers (only using 0s and 1s): ")
          integer_strings = binary_strings.split(",")
          decimal_number=[]
          for binary in integer_strings:
              decimal_number = decimal_number + [str(int(binary, 2))] 
              if binary==integer_strings[:-1]: 
                  break
          print(",".join(decimal_number))
          break
          
      except:
          print("{} is not a binary number.".format(binary))
          pass

main()
  

