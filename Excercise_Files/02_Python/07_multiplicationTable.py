# simple program that gives you the 10 times multiplication table of a chosen number

# user input
base = int(input('Which whole number do you choose for your multiplication table? '))

# a while loop will do the multiplication 10 times
# fortunately on the way we can use 'i' from the condition to multiply our chosen number with
i = 1
while i < 11:
  print(base, 'x', i, '=', base * i)
  i += 1
