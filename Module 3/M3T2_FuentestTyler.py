# M3T2 - Doctest
# CSC 221
# Tyler Fuentes
# 09/20/2021
'''
The goal here is to:
    a. Make a simple calculator
    b. Use Doctest to automatically test them
'''

# This function will test addition function of calulator
def add(a, b): 
    
    '''
add() - add two numbers.

    Parameters
    ----------
    a: int
    b: int
    
    Returns
    ----------
    int, the sum of a and b
    
    Doctests:
    >>> add (2, 2)
    4
    >>> add (1, -1)
    0
    >>> add (1.5, 0.5)
    2.0
    
    '''
    return a + b

# This function wil test for multiplication 
def multiply(a, b):
    """
    multiplies two numbers.
    Tests:
    >>> multiply (3, 2)
    6
    >>> multiply (1, -1)
    -1
    >>> multiply (2.5, 1.5)
    3.75
    
        
    """
    return a * b
# This function tests for absolute value
def abs(value):
    """
    Absolute value of the number.
    >>> abs(-5)
    5
    >>> abs(-1)
    1
    
    """
    if value < 0:
        return -value
    else: 
        return value

    

# This is to load and run the doctest automatically
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    