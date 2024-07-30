import numpy as np
import math

print('array with shape (4, 3) all zeros')
array_zeros = np.zeros((4, 3))
print(array_zeros)

print('array with shape (4, 3) all ones')
array_ones = np.ones((4, 3))
print(array_ones)

print('array with shape (4, 3) numbers from 0 to 11')
array_random = np.arange(0, 12).reshape(4, 3)
print(array_random)

print()
print('Tabulate the following function: F(x)=2x^2+5, x∈[1,100] with step 1.')
print(np.column_stack((np.arange(1, 101), 2 * (np.arange(1, 101).reshape(100, 1) ** 2) + 5)))

print()
print('Tabulate the following function: F(x)=e^−x, x∈[−10,10] with step 1.')

x = np.arange(-10, 11).reshape(21, 1)
result = np.exp(-x)
for i in range(len(x)):
    print(f'{x[i]} = {result[i]}')




