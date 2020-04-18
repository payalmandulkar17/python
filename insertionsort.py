A=[5,4,3,2,1]
for i in range(len(A)):
    value=A[i]
    hole=i
    while(hole>0 and A[hole-1]>value):
        A[hole]=A[hole-1]
        hole=hole-1
    A[hole]=value
print(A)        