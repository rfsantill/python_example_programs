import sys
"""
Python program to find the largest element and its location.
"""

def largest_element(a, loc):
    """ Return the largest element of a sequence a.
    """
    try:
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
    except TypeError:
        print("Could not convert data to an integer.")
        return -1
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise


if __name__ == "__main__":

    a = [1,2,3,2,1]
    loc = True
    print("Largest element is {:}".format(largest_element(a, loc)))
    
