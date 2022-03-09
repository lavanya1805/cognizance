# question 2
import numpy as np
x = np.random.randint(0,2,6)
print("First array:")
print(x)
y = np.random.randint(0,2,6)
print("Second array:")
print(y)
print("check if they are equal")
array_equal = np.allclose(x, y)
print(array_equal)
