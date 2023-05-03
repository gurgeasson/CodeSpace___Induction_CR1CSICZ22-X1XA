''' this program checks if a number is prime or not, and is based on
https://www.programiz.com/python-programming/examples/prime-number '''

# user input
n = int(input("Enter a number: "))

# prime numbers are greater than 1
if n > 1:
  # iterate from 2 to n and check for factors
  for i in range(2,n):
    # if we find a number that divides n with remainder, we found a not prime
    if (n % i) == 0:
      print(n,"is not a prime number")
      print(i,"times",n//i,"is",n)
      break
    # otherwise prime
    else:
       print(n,"is a prime number")

# input is less or equal to 0 there for not a prime number
else:
   print(n,"is not a prime number")
