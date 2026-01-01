import numpy as np
'''
2,2,3
[
    [
        [0 0 0]
        [0 0 0]
    ]

    [   [0 0 0]
        [0 0 0]
    ]
] 


[   
    [
        [0 0 0]
        [0 0 0]
    ]
]
'''
# a = np.zeros((2,2,2),dtype='int32')
# print(a.dtype,'\n')
# print(a,'\n')
# print(a.shape,'\n')
# print(a.ndim,'\n')


# b = np.ones((1,2,3,4,4))
# print(b.dtype,'\n')
# print(b,'\n')
# print(b.shape,'\n')
# print(b.ndim,'\n')
#
# c = np.full((2,3),233,dtype='float32')
# print(c.dtype,'\n')
# print(c,'\n')
# print(c.shape,'\n')
# print(c.ndim,'\n')
#
# d = np.full_like(a,55)
# print(d.dtype,'\n')
# print(d,'\n')
# print(d.shape,'\n')
# print(d.ndim,'\n')
#
# e = np.arange(2,10,2)
# print(e.dtype,'\n')
# print(e,'\n')
# print(e.shape,'\n')
# print(e.ndim,'\n')

# f = np.eye(3,3,0)
# print(f.dtype,'\n')
# print(f,'\n')
# print(f.shape,'\n')
# print(f.ndim,'\n')

# g = np.linspace(0,10,5)
# print(g.dtype,'\n')
# print(g,'\n')
# print(g.shape,'\n')
# print(g.ndim,'\n')

# g = np.random.rand(2,2)
# print(g.dtype,'\n')
# print(g,'\n')
# print(g.shape,'\n')
# print(g.ndim,'\n')

# g = np.random.randint(1,7,(3,3))
# print(g.dtype,'\n')
# print(g,'\n')
# print(g.shape,'\n')
# print(g.ndim,'\n')

# g = np.identity(4)
# print(g.dtype,'\n')
# print(g,'\n')
# print(g.shape,'\n')
# print(g.ndim,'\n')

# g = np.array([[1,2,3],[1,2,3],[1,2,3]])
# g = np.repeat(g,2,)
# print(g.dtype,'\n')
# print(g,'\n')
# print(g.shape,'\n')
# print(g.ndim,'\n')

# g = np.array([[1,2,3],[0,0,0],[1,2,3],[1,2,3]])
# print(np.reshape(g,(3,4)),'\n********')
# print(np.reshape(g,(4,3)),'\n********')
# print(np.reshape(g,(2,2,3)),'\n********')
# print(np.reshape(g,(3,2,2)),'\n********')
# print(np.reshape(g,()),'\n********')
# print(g)

g = np.array([[1,2,3],[4,5,6]])
h=np.array([[7,8,9],[10,11,12]])
print('vstack')
print(np.vstack([g]),'\n')
print(np.vstack([g,h,h,g]),'\n')

print('hstack')
print(np.hstack([g]),'\n')
print(np.hstack([g,h,h,g]))
