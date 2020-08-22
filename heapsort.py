#ヒープソート
A = {1:20,2:50,3:10,4:30,5:70,6:40,7:60,8:80}

def INSERT(i):
    num = N # 2
    o = 1
    while  o != 0:
        o = num // 2 # 1
        if A[num] > A[o]:
            work = A[num]
            A[num] = A[o]
            A[o] = work
            num = o
        if A[num] <= A[o]:
            o -=1


    return A


for N in range(2,9,1):
    hoge = INSERT(N)
print ('ヒープ作成結果')
print(hoge)


def heap (hani):#7
    oya = 1
    kodo = oya * 2 #2
    while  kodo < hani: #2>7 再構成ループ
        if kodo+1 <= hani: #3<7
            if hoge[kodo+1] > hoge[kodo]:#60 > 70
                kodo+=1

        if hoge[kodo] > hoge[oya]: #3[60] > 2[70]
            work = hoge[kodo]
            hoge[kodo] = hoge[oya]
            hoge[oya] = work
            oya = kodo
            kodo = oya*2
        elif hoge[kodo] <= hoge[oya]:
             kodo = hani + 1

    return hoge


for s in range(len(hoge),2,-1):
    work = hoge[1]
    hoge[1] = hoge[s]
    hoge[s] = work
    #print(hoge)
    if s > 2:
        hoge= heap(s-1)
print ('ヒープソートを昇順に並び替え')
print(hoge)
