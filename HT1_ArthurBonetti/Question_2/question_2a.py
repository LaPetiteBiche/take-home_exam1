import numpy as np 

# 1st method


def function_to_vector(array):
    return (np.array(array**3 + array*np.exp(array) + 1))


new_array = function_to_vector(np.array([2, 3, 1], dtype=np.float32))
print(new_array)

# 2nd method

array = np.array([2, 3, 1], dtype=np.float32)
x = 0
for v in array:
    array[x] = v**3 + v * np.exp(v) + 1
    x += 1
print(array)

# Check

print (new_array == array)