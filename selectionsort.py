#P:148
#小さい順から並べていく
A =[5,4,2,1,3]
N =5

for I in range(0,5,1):
    min = I
    for J in range(I+1,5,1):
        if A[min] > A[J]:
            min = J
    work = A[I]
    A[I] = A[min]
    A[min] = work
print(A)

#大きい順から並べていく

A =[5,4,2,1,3]
N =4

for I in range(N,0,-1):
    MAX = I
    for J in range(I-1,-1,-1):
        if A[MAX] < A[J]:
            MAX = J
    work = A[I]
    A[I] = A[MAX]
    A[MAX] = work
print(A)
