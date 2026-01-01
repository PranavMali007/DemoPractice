import numpy as np

matrix = [
  [
    [1, 2],
    [3, 4]
  ],
  [
    [],
    [[5]]
  ]
]

for i in matrix:
    print(i)
    print()
    for j in i:
        print(j)
        print()
        for k in j:
            print(k)
            print()
array3D = [
  [
    [2, 4],
    [6, 8]
  ],
  [
    [10, 12],
    [14, 16]
  ]
]

for l,f in np.nditer(array3D):
    print(l,f)
for l in np.nditer(array3D):
    print(l)
for l,f in np.ndenumerate(array3D):
    print(l,f)