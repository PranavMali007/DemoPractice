from email.contentmanager import raw_data_manager
from traceback import print_tb

import numpy as np
data = [12, 45, 78, 23, 56, 19, 34, 27, 20, 21, 43, 65, 87, 32, 54, 46, 98, 11, 33, 55]
with open('raw_data.txt','w') as file:
    for i in range(0,len(data),5):
        line = ','.join(str(num) for num in data[i:i+5])
        file.write(line + '\n')

matrix_format = np.genfromtxt('raw_data.txt',delimiter=',')
print(type(matrix_format[0][0]))
print(matrix_format , '\n')
file = matrix_format.astype('int32')
print(type(file[0][0]))
print(file,'\n')


print(matrix_format>50,'\n')
print(np.any(matrix_format > 50, axis=0))#IN COLUMN ANY ONE VALUE SHOULD BE >50=TRUE
print(np.any(matrix_format > 50, axis=1))#IN ROW ANY ONE VALUE SHOULD BE >50=TRUE
print(np.all(matrix_format > 30, axis=0))#IN COLUMN ALL VALUE SHOULD BE >50=TRUE
print(np.all(matrix_format > 30, axis=1))#IN ROW ALL VALUE SHOULD BE >50=TRUE
'''
[[12 45 78 23 56]
 [19 34 27 20 21]
 [43 65 87 32 54]
 [46 98 11 33 55]]  
'''