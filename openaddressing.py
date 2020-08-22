#ハッシュ表
#P:177

H =[219,-1,532,463,142,-1,-1,-1,298,308]

d = 223
n = (d % len(H))
m = n
flg = 0

while flg == 0:
    if H [m] == d:
        flg = H[m]
        break
    else:
        if H[m] == -1:
            flg = -1
        else:
            m+=1
            if m == 10:
                m = 0

            elif m == n:
                flg = -1
if flg > 0:
    print('探索成功',+m)
else:
    print('該当データなし')

#チェイン法
#P:181
#オープンアドレス法で空いているところに格納されている時に次のレコードの場所にいくやつ
H = [110,111,112,113,114,120,130]
P = [5,0,0,0,0,6,-1]

d = 130
n = d % 5
flg = 0


while n != -1 and flg == 0:
    if H[n] == d:
        flg = n
    else:
        n = P[n]

if flg > 0:
    print('探索成功',+n)
else:
    print('該当データなし')
