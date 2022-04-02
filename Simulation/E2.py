# Import commands
"""
This section shows how to import "standard" python modules or parts of the modules.
"""

## import complete module without renaming it
import numpy
print(numpy.pi)
print(numpy.sin(numpy.pi))

## import only one function from a module
from numpy import pi
print(pi)

## import all functions of a module without module name
from numpy import *
print(sin(pi))

## import complete module and renaming it
import numpy as np
print(np.pi)
print(np.sin(np.pi))

## import only one function of a module and renaming it
from numpy import pi as ip
print(ip)

## customized modules and concept of __int__.py
"""
This subsection gives an introduction how to import customized modules and the use of 
an __init__.py.
"""
### get custom modules out of the same directory
import E2_fun as Get
Get.fun_test(1)

"""importing directory"""
import resources # here is no problem
"""new variable name = directory.file including the function.function()"""
test = resources.FunOne.one()
"""Here arises an Error ... module '..' has no attribute '..' ..."""

"""from directory.file import function"""
from resources.FunOne import one
from resources.FunTwo import two
test1 = one()
test2 = two()

"""
- importing a lot of files or modules can be simplified by using __init__.py
- the __init__.py runs as soon as a module gets imported, the import command is 
  looking for a __init__.py file
- __init__.py gather various files together to be included in one module
"""

import resources  # runs __int__.py
test1 = resources.one()
test2 = resources.two()

# Data types of python
"""
Only data types important for this course are introduced for more information 
check, e.g., https://www.w3schools.com/python/python_datatypes.asp 
"""

## Data types
"""
In python integers (int), floats (float), and complex numbers (complex) are 
available to define single values.
"""

intVal = 1
floatVal = 1.0
complexVal = 1j

"""
In python lists, tuples, and sets are available to define groups of values. 
Be careful with the different types of brackets!
"""

listVals = [0, 1, 2, 3, 4, 5, 5]
tupleVals = (0, 1, 2, 3, 4, 5, 5)
setVals = {0, 1, 2, 3, 4, 5, 5}

print(listVals)
print(tupleVals)
print(setVals)

"""nice to use unpack function:"""
a, b, c, d, e, f, g = tupleVals

print([a, b, c, d, e, f, g])


### non native data types
"""
using numpy arrays you can build n-dimensional arrays, 
e.g., 1-D array / a vector or a 2-D array / a matrix...
Numpy arrays are faster and smaller (less memory) than lists.
"""
import numpy as np

npArrayVector = np.array([0, 1, 2, 3, 4, 5, 5])

npArrayMatrix = np.array([[0, 1, 2, 3, 4, 5, 5],
                        [0, 1, 2, 3, 4, 5, 5]])

## How to address/index group elements -> [row, column] or [row][column]
"""
  0    1    2    3    4    5    6    7    8
  ↓    ↓    ↓    ↓    ↓    ↓    ↓    ↓    ↓
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
  ↑    ↑    ↑    ↑    ↑    ↑    ↑    ↑    ↑
 -9   -8   -7   -6   -5   -4   -3   -2   -1
"""


"""first row, first column"""
print(npArrayMatrix[0, 0])

"""third row, fourth column"""
print(npArrayMatrix[1, 3])

"""first row, last column"""
print(npArrayMatrix[0, -1])
print(npArrayMatrix[0, 6])

"""various elements"""
print(npArrayMatrix[0, 1:3:5])

"""range of elements: first row, from second column to fourth column"""
print(npArrayMatrix[0, 1:4])

"""complete first row"""
print(npArrayMatrix[0, :])

## Function
"""There are two types of functions:
    - "normal" functions
    - lambda functions (also called anonymous functions)
"""

### normal functions
"""see example E2_fun.py"""

### lambda function
y = lambda x : x**2 + 5
print(y(2))

## classes
"""
Comment object oriented programming: https://www.youtube.com/watch?v=DlphYPc_HKk
This goes beyond the scope of the present course...
"""

# Structures and Loops
## if
x = 5

if x <= 5:
    print('true')

## for
newList = ["one", "two", "three", "four"]
for ii in newList:
    print(ii)

## while
counter = 0

while counter <= 5:
    print(counter)
    counter = counter + 1
    # counter += 1

# Basic operations
import numpy as np

## Scalars
x = 5 + 5
x = x - 5
x = x * 5
x = x / 5
x = 5**5
x = np.power(5,5)
x = x**(1/2)
x = np.sqrt(4)
x = np.cbrt(27)
x = np.power(27,1/3)

## Arrays / vectors / matrices
"""
Arrays can be treated in two ways:
    - element wise
    - or with matrix operations
"""

### Element wise operations
import numpy as np
testArray = np.array([1,2,3])
print(testArray)
print(testArray + 1)
print(testArray - 1)
print(testArray * 2)
print(testArray * testArray)
print(np.multiply(testArray,2))
print(testArray / 2)
print(testArray / testArray)
print(np.divide(testArray,2))

### Vector / Matrix operations
"""
- np.cross
- np.dot
"""

### numerical integration and di
"""Integration of a vector with the trapezoidal rule."""
print(np.trapz([1,2,3]))

"""Numerical calculation of first difference"""
print(np.diff(np.array([1, 2, 4, 7, 0])))

# Debugging in PyCharm
## print
"""
The print() function is really important! The function is part of python.
"""

## Debugger
"""
PyCharm offers a debugger with variable viewer and the option to 
track variables (add watch -> Special variables). This option belongs 
to PyCharm and is not originating from python. 
So, no PyCharm - no/different debugger.
"""

# Plotting
import matplotlib.pyplot as plt
import numpy as np

y = lambda t: 0.5 * t**2 + 2
time = np.linspace(0, 10, 100)

plt.figure()
plt.plot(time, y(time))
plt.plot(time, y(time)+1)
plt.xlabel('time')
plt.ylabel('y')
plt.show()


# Exercise
"""
- create a sine and cosine function for x = {0:0.1:2*pi}
- plot both function in one plot
- show that d/dx sin(x) == cos(x) 
"""


# Jupyter Notebook
"""
Let's switch to Jupyter Notebook
"""
