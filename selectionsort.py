A=[5,4,3,2,1]
print("hello")
for i in range(len(A)-1):
    min=i
    for j in range(i+1,len(A)):
        if(A[j]<A[min]):
            min=j
    temp=A[i]
    A[i]=A[min]
    A[min]=temp
print(A)    