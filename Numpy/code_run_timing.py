import time
import numpy as np
start = time.time()
var = np.array([1,2,3,4,5])
varsqr = var**2
print(varsqr)
end = time.time()
timing_1=end - start
print("Vectorized timing_1", timing_1)

print('*******************************************')

start = time.time()
lst= [1,2,3,4,5]
for i in range(len(lst)):
    sqr = i**2
    print(sqr)
end = time.time()
timing_2=end - start
print("Vectorized timing_2", timing_2)
print('*******************************************')
start = time.time()
lst= [1,2,3,4,5]
lst = np.array(lst)
sqr = lst**2
print(sqr)
end = time.time()
timing_3=end - start
print("Vectorized timing_3", timing_3)
print('*******************************************')

max_time = [timing_1,timing_2,timing_3]
max_time.sort()
print("Vectorized timing_1", timing_1)
print("Vectorized timing_2", timing_2)
print("Vectorized timing_3", timing_3)
print('max_time=',max_time)