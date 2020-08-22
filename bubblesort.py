#バブルソート
#P:152

A = [4,2,5,1,3,6,8,7,6,]
N =len(A)
for i in range(N,1,-1):

    for k in range(0,i-1,+1):
        if A[k] > A[k+1]:
            work = A[k]
            A[k] = A[k+1]
            A[k+1] = work
print(A)
