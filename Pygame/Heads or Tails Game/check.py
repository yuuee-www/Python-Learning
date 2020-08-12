from pythonds.basic.queue import Queue


def check(): # Code for checking the results
  ans_check = input('Do you want to print the result in dorder they were played or sorted? \n \
                               [Enter "o" for in order and "s" for sorted]\n')
  if ans_check == 'o':
  
    f = open('result.txt','r') # Another way to operate file I/O
    result = Queue() 
    for line in open('result.txt'):
        line = line.strip() # To make the output more clear 
        result.enqueue(line)
    while result.size()>1:
        print(result.dequeue())
    f.close()




    
  if ans_check == 's':
   
    f = open('result.txt','r')
    result = []    # Read lines and store it as a list
    for line in open('result.txt'): 
        line = line.strip()    
        result.append(line)
    result.sort()   # Sorted 
    for item in result:
      print(item)
    f.close()  

check()
