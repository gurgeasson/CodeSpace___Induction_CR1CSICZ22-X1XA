# simple program that list the Fibonacci series between 0 to 50

# Revisiting the Fibonacci Series after learning about Lists

# initiate array with first two number
fiboSerie = [0, 1]

# initiate array item index
i = 0
while i < 50:
   # use variable i to identify the preceding two numbers for next in line
   # check if we have reached our target, if so, terminate
  if fiboSerie[i] + fiboSerie[i + 1] > 50:
    break
  # calculate next in series and add it to list
  fiboSerie.append(fiboSerie[i] + fiboSerie[i + 1])
  # increment the count
  i += 1

# print the List
print(fiboSerie)


'''
# here you can find the original program before Lists

# set variables
x = 0 # the series starts with two given numbers. first number 'x'
y = 1 # second 'y'. later I use these variables to store the successive numbers in the series.
z = x + y # I calculate and store the successive number as 'z'

print(x) # print first two numbers of the series
print(y)

""" set up loop to print successive numbers in series, next transverse series with 'x' and 'y', than calculate next number in series. do it till z < 50 """
while z < 50:
  print(z)
  x = y
  y = z
  z = x + y '''
