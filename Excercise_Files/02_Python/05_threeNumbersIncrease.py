# simple program that takes three numbers from user, and tells if they increase/decrease/neither

# user input three numbers
num1 = int(input('Input the first whole number: '))
num2 = int(input('Input the second whole number: '))
num3 = int(input('Input the third whole number: '))

# check if decreasing
if num1 > num2 and num2 > num3: # if order decrease
  print('Decreasing order')
# or increasing
elif num1 < num2 and num1 < num3: # if order increase
  print('Increasing order')
# or neither increasing or decreasing
else: # if neither of the above
  print('Neither increasing or decreasing order')
