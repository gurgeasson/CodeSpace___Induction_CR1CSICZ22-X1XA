# this program calculates the factorial of a number

# this function takes a number and calculates it's n!
def factorial_function(num):
  i = num
  #print (i)
  f = 1
  # iterate form num to 1 and multiply each whole number with factorial on the way
  while i > 0:
    f *= i
    i -= 1
  #print (f)
  return f

# user input
n = int(input('input a positive whole number: '))

if n < 0: # quick check if input int is not negative
  n = int(input('try again\ninput a positive whole number: '))

# call function and print the result
print(str(n) + '! equals ' + str(factorial_function(n)))
