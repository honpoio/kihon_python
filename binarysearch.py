#binarysearch.py
#二分探索法
#P:169
T =[1,4,7,9,12,18,22]

idx = 0
L = 0
H = len(T)
Tkey =18
while idx == 0 and L <= H:
    M = (L+H) // 2
    if Tkey == T[M]:
        idx = M
    if Tkey < T[M]:
        H = M - 1
    else:
        L = M + 1


print(str(Tkey)+'は配列Tの添字'+str(idx)+'にあります')


#番兵
#P:164
name =['まき','太郎','nana','syoko']
num = 'まき'
N = 3
name.insert(len(name),num)
hoge =0

for i in range(0,len(name),+1):
    if  name[i] != num:
        hoge+=1

if  hoge > N:
    print('該当データなし')
else:
    print('該当データあり')
