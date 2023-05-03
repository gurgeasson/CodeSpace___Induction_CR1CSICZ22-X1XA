# this program employs two functions. one to print list content, the other to find max value

# print function
def print_function(toPrintInput):
  print('The content of the list is:', toPrintInput)

# find max value of an array function
def findMax_function(findMaxInput):
 findMaxInput.sort()
 print('The max value in the list:', findMaxInput[len(findMaxInput) - 1]) # find and print Max value

# declare list
funcList = [10, 2, 3, 4, 7] # input

# call functions
print_function(funcList)
findMax_function(funcList)
