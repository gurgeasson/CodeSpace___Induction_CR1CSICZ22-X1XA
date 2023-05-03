# this program finds the Min and Max of a list

# declare list
minMaxList = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49] # input

# print original list before sorting
print('Original List:', minMaxList)

# sort list ascending
minMaxList.sort()

# find and print Max value
print('Maximum value for the above list =', minMaxList[len(minMaxList) - 1])
# find and print Min value
print('Minimum value for the above list =', minMaxList[0])
