# this program calculates the average of all values of a list

# declare list
listToAvg = [20, 30, 25, 35, -16, 60, -100]

# declare variable sum
sum = 0
# iterate through list and sum all elements
for x in listToAvg:
  sum += x
# declare variable avg and calculate average of list
avg = sum / len(listToAvg)
# print result
print('Average value of the list elements is:', avg)
