#クイックソートを用いた配列ソート
#基準値を決めてそれ以上かそれ以下かわけていくソート方法
#再帰関数

A = [2,4,221,5,8,2,9,10]
K = 0
J = 0
def Arrange(A,min,max,pivot):
    L = min
    R = max
    while L <= R:
        tmp = A[L]
        A[L] = A[R]
        A[R] = tmp
        while A[L]< pivot:
            L+=1
        while A[R]>= pivot:
            R -=1

    ret = L
    return ret

def findpivot(A,min,max):
    pivot = A[min]
    K  = min+1
    ret = -1
    found = False
    while K <= max and not found:
         if A[K] == pivot:
             K+=1
         else:
             found = True
             if A[K]> pivot:
                 ret = K
             else:
                 ret = min
    return ret

def quicksort(A,min,max):
    J=findpivot(A,min,max)
    if J > -1:
        pivot = A[J]
        K = Arrange(A,min,max,pivot)
        L = K - 1
        quicksort(A,min,L)
        quicksort(A,K,max)
        return(A)

num = quicksort(A,0,len(A)-1,)
print(num)
