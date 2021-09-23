"""
Python program to find the largest element and its location.
"""

def largest_element(a, loc):
    """ Return the largest element of a sequence a.
    """
    largest = a[0]
    location = 0
    for i in range(0,len(a)):

        if largest <= a[i]:
            largest = a[i]
            if loc == True:
                location = i

    if loc == True:
        return largest, location
    else:
        return largest
    


if __name__ == "__main__":

    a = [1,2,3,2,1]
    loc = True
    print("Largest element is {:}".format(largest_element(a, loc)))
    
