#シェルソート
#なんか奇数偶数的なn数とばした要素で比較するやつ
H  = [2,1,3,8,6]

k = (len(H))// 2
u =0
while k != 0:
    s = k
    while s <= len(H)-1:
        u = s - k #
        while u >=0:
            if H[u] > H[u+k]:
                print(H)
                work = H[u]
                H[u] = H[u+k]
                H[u+k] = work
                u = u - k
            else:
                break

        s = s + 1

    k = k // 2
print(H)
