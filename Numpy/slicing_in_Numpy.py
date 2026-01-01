import numpy as np

'''
    Index	Value	        Description	
c[1, :, :]	c[1]	        Selects the entire second block (index 1). 
                            The : selects all rows and all columns within that block.	
c[1, 0, :]	[21, 31, 41]	Selects the second block (index 1) and
                            the first row (index 0) within it.	
c[1, 1, 2]	51	            Selects the element at second block (index 1),

c[0] // is a two-dim array
c[0][1] // is a one-dim array
c[0][1][0] // is a value
'''
c = np.array([
    [
        [12, 14, 15, 43],
        [16, 17, 18, 5],
    ],
    [
        [21, 31, 41, 57],
        [31, 41, 51, 9]
    ],
    [
        [65, 75, 3, 9],
        [5, 2, 66, 76],
    ]
])

print(c.shape,"\n")
# (3, 2, 4)
print(c[1], '\n')
# [[21 31 41 57]
#  [31 41 51  9]]
print(c[2, 1], '\n')
# [ 5  2 66 76]
print(c[0, :], '\n')
# [[12 14 15 43]
#  [16 17 18  5]]
print(c[2, 1:], '\n')
# [[ 5  2 66 76]]
print(c[1, 0, 1], '\n')
# 31
print(c[0, 0, :2])
# [12 14]
print(c[0, ::-1])
# [[16 17 18  5]
#  [12 14 15 43]]
print(c[1, 0, ::-1])
# [57 41 31 21]

print('#####################################################')
d_array = np.array(
    [
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ],
        [
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
    ])
print(d_array.shape, '\n')
# (2, 2, 4)
print(d_array.ndim, '\n')
# 3
print(d_array[0], '\n')
# [[1 2 3 4]
# [5 6 7 8]]
print(d_array[0][1], '\n')
# [5 6 7 8]
print(d_array[0][1][0], '\n')
# 5
