# simple program that takes three numbers from user
# than tells if all equal, all different or in-between

# user input three numbers
num1 = int(input('Input the first whole number: '))
num2 = int(input('Input the second whole number: '))
num3 = int(input('Input the third whole number: '))

#  check if they are all equal
if num1 == num2 and num1 == num3: # if all equal print all equal
  print('All numbers are equal')
# check if they are all different  
elif num1 != num2 and num1 != num3 and num2 != num3: # if all different print all different
  print('All numbers are different')
# if neither of the above, fall back to this
else: # if some are equal and some are not, print 'Neither all are equal or different'
  print('Neither all are equal or different')
