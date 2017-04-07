
'''
Playing with the numpy library
'''

import numpy as np

if False:
        array = np.array([1,4,5,8],float)
        print array
        print ""
        array = np.array([[1,2,3],[4,5,6]],float)  #a 2d array/Matrix
        print array

'''
You can index, slice, and manipulate a Numpy array much like you would
a Python list.
'''

if False:
    array = np.array([1,4,5,8],float)
    print array
    print ""
    print array[1]
    print ""
    print array[:2]
    print ""
    array[1]=5.0
    print array[1]

# Change False to True to see matrix indexing and slicing in action
if False:
    two_D_array = np.array([[1,2,3],[4,5,6]],float)
    print two_D_array
    print ""
    print two_D_array[1][1]
    print ""
    print two_D_array[1, :]
    print ""
    print two_D_array[:, 2]

'''
Here are some basic arithmetric operations that you can do with Numpy arrays
'''
# Change False to True to see Matrix arithmetrics in action
if False:
    array_1 = np.array([1,2,3],float)
    array_2 = np.array([5,2,6],float)
    print array_1 + array_2
    print ""
    print array_1 - array_2
    print ""
    print array_1 * array_2

    
'''
In addition to the standard arithmetic operations, Numpy also has a range of
other mathematical operations that you can apply to Numpy arrays, such as
mean and dot product.

Both of these functions will be useful in later programming quizzes.
'''
if True:
    array_1 = np.array([1,2,3], float)
    array_2 = np.array([[6],[7],[8]], float)
    print np.mean(array_1)
    print np.mean(array_2)
    print ""
    print np.dot(array_1, array_2)
