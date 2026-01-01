rows = int(input("Enter number of rows: "))

for i in range(0,rows):
    print('*' * (rows-i))
print('______________________________')
for j in range(rows,0,-1):
    print(" "*(rows-j) + "*"*j)
print('______________________________')
for k in range(rows,0,-1):
    print(" "*(rows-k) + "*"*(2*k-1))
print('______________________________')
for l in range(1,rows):
    print(" "*(rows-l) + "*"*(2*l-1))

print('______________________________')
for l in range(1,rows):
    if l==((rows+1)//2):
        print(f"{' ' * ((rows+1)//2)}WELCOME")
        break
    else:
        print(" "*(rows-l) + "*"*(2*l-1))

for m in range(rows,1,-1):
    print(" "*(rows-m) + "*"*(2*m-1))