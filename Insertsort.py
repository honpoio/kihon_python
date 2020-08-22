#挿入ソート
M = [0] * 5
N = 0
J = 0
BUF = [4,2,5,1,3]
for i in range(0,5,1):
    I =0
    while I <=N and M[I] > BUF[i]:
        I = I+1
    J = N
    while J >= I:
        M[J] =M[J-1]
        J = J-1
    M[I] = BUF[i]
    N = N + 1
print(M)
