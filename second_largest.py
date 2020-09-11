"""
 Python program to find second largest value in a list, e.g., given

  [3, 2, 5, 2, 4]

find 4 and, possibly, its location (4).

Source: www.geeksforgeeks.org/python-program-to-find-second-largest-number-in-a-list/
"""

# number in a list

# list of numbers - length of list should be at least 2
list1 = [10, 20, 4, 45, 99]

mx=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
n =len(list1)
for i in range(2,n):
    if list1[i]>mx:
        secondmax=mx
        mx=list1[i]
    elif list1[i]>secondmax and mx != list1[i]:
        secondmax=list1[i]
    else:
        if secondmax == mx:
            secondmax = list1[i]

print("Second highest number is : ",str(secondmax))
