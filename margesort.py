#python margesort.py
 #-*- coding: utf-8 -*-
output =[47,33,68,55,74,89,25,10]

span_size =2　#分割範囲を設定
size = len(output)　#outputの要素数を代入
size2 = size // 2
temp = [0]*size2    #入れ替えに使用する配列の大きさを設定

while span_size <= size: #分割範囲のソートが終わったら実行,配列範囲を指定する➀
    span_idx = 0　#初期化   #分割する位置を指定
    write_idx = 0　#初期化　#入れ替えの値
    while span_idx < size: #分割の位置を設定②
        a_idx = span_idx #分割した範囲の要素を比較
        b_idx = span_idx + span_size // 2 #分割した範囲内の比較対象を設定
        #print(a_idx)
        #print('a_idxを初期化')
        #print(b_idx)
        #print('b_idxを初期化')
        #print(span_size)
        #print('span_sizeの値')
        #print(span_idx)
        #print('span_idxの値')

        for i in range(a_idx - span_idx,b_idx - a_idx,1): #入れ替える要素を設定③
            temp[i] = output[i+span_idx]
            #print(temp)
            #print('配列tempに追加')
            a_yet = True
            b_yet = True
        while a_yet == True or b_yet == True:#分割範囲内のソートが終わったらループ終了④
            if b_yet == False or (a_yet == True and b_yet == True and temp[a_idx - span_idx] <= output[b_idx]):#⑤
                #短絡評価,最初から教えて欲しい,,,時間めちゃめちゃ食ったんだけど,,,,
                #
                #print(output)
                output[write_idx] = temp[a_idx - span_idx]
                #print(output)
                #print('比較対象tempよりoutputの方が大きい場合outputに配列をコピー')
                a_idx +=1
                #print(a_idx)
                #print('変数a_idxにカウント')
                if a_idx >= span_idx + span_size // 2:#配列tempの要素を全て整列できた時,もしくは走査範囲が終了した時⑦
                    a_yet = False
                    #print('a_yetをfalseにする')
            else:
                #temp[a_idx - span_idx] > output[b_idx]の時
                #print(output)
                output[write_idx] = output[b_idx]
                #print(output)
                #print('比較対象tempよりoutputの方が小さい場合outputに配列をコピー')
                b_idx +=1
                #print(b_idx)
                #print('変数b_idxにカウント')
                if b_idx >= span_idx + span_size:#配列tempの要素が全て整列されている時⑥
                    b_yet = False
                    #print('b_yetをfalseにする')

            write_idx+=1  #代入位置をカウント
            #print(write_idx)
            #print('変数write_idxにカウント')


        span_idx = span_idx + span_size#ソートが終わったら次の走査範囲へ移動
        #print(span_idx)
        #print('span_idx+span_sizeを足してソートする場所を変更')


    span_size = span_size * 2#
    #print(span_size)
    #print('範囲を2乗する')


print(output)

"""###########################################################################
##output =[47,33,68,55,74,89,25,10]の時

0
a_idxを初期化
1
b_idxを初期化
2
span_sizeの値
0
span_idxの値
[47, 0, 0, 0]
配列tempに比較対象を追加
[47, 33, 68, 55, 74, 89, 25, 10]
[33, 33, 68, 55, 74, 89, 25, 10]
比較対象tempよりoutputの方が小さい場合outputに配列をコピー
2
変数b_idxにカウント
b_yetをfalseにする
1
変数write_idxにカウント
[33, 33, 68, 55, 74, 89, 25, 10]
[33, 47, 68, 55, 74, 89, 25, 10]
比較対象tempよりoutputの方が大きい場合outputに配列をコピー
1
変数a_idxにカウント
a_yetをfalseにする
2
変数write_idxにカウント
2
span_idx+span_sizeを足してソートする場所を変更
2
a_idxを初期化
3
b_idxを初期化
2
span_sizeの値
2
span_idxの値
[68, 0, 0, 0]
配列tempに比較対象を追加
[33, 47, 68, 55, 74, 89, 25, 10]
[33, 47, 55, 55, 74, 89, 25, 10]
比較対象tempよりoutputの方が小さい場合outputに配列をコピー
4
変数b_idxにカウント
b_yetをfalseにする
3
変数write_idxにカウント
[33, 47, 55, 55, 74, 89, 25, 10]
[33, 47, 55, 68, 74, 89, 25, 10]
比較対象tempよりoutputの方が大きい場合outputに配列をコピー
3
変数a_idxにカウント
a_yetをfalseにする
4
変数write_idxにカウント
4
span_idx+span_sizeを足してソートする場所を変更
4
a_idxを初期化
5
b_idxを初期化
2
span_sizeの値
4
span_idxの値
[74, 0, 0, 0]
配列tempに比較対象を追加
[33, 47, 55, 68, 74, 89, 25, 10]
[33, 47, 55, 68, 74, 89, 25, 10]
比較対象tempよりoutputの方が大きい場合outputに配列をコピー
5
変数a_idxにカウント
a_yetをfalseにする
5
変数write_idxにカウント
[33, 47, 55, 68, 74, 89, 25, 10]
[33, 47, 55, 68, 74, 89, 25, 10]
比較対象tempよりoutputの方が小さい場合outputに配列をコピー
6
変数b_idxにカウント
b_yetをfalseにする
6
変数write_idxにカウント
6
span_idx+span_sizeを足してソートする場所を変更
6
a_idxを初期化
7
b_idxを初期化
2
span_sizeの値
6
span_idxの値
[25, 0, 0, 0]
配列tempに比較対象を追加
[33, 47, 55, 68, 74, 89, 25, 10]
[33, 47, 55, 68, 74, 89, 10, 10]
比較対象tempよりoutputの方が小さい場合outputに配列をコピー
8
変数b_idxにカウント
b_yetをfalseにする
7
変数write_idxにカウント
[33, 47, 55, 68, 74, 89, 10, 10]
[33, 47, 55, 68, 74, 89, 10, 25]
比較対象tempよりoutputの方が大きい場合outputに配列をコピー
7
変数a_idxにカウント
a_yetをfalseにする
8
変数write_idxにカウント
8
span_idx+span_sizeを足してソートする場所を変更
4
span_size自身を*2して次の分割地点に移動
0
a_idxを初期化
2
b_idxを初期化
4
span_sizeの値
0
span_idxの値
[33, 0, 0, 0]
配列tempに比較対象を追加
[33, 47, 0, 0]
配列tempに比較対象を追加
[33, 47, 55, 68, 74, 89, 10, 25]
[33, 47, 55, 68, 74, 89, 10, 25]
比較対象tempよりoutputの方が大きい場合outputに配列をコピー
1
変数a_idxにカウント
1
変数write_idxにカウント
[33, 47, 55, 68, 74, 89, 10, 25]
[33, 47, 55, 68, 74, 89, 10, 25]
比較対象tempよりoutputの方が大きい場合outputに配列をコピー
2
変数a_idxにカウント
a_yetをfalseにする
2
変数write_idxにカウント
[33, 47, 55, 68, 74, 89, 10, 25]
[33, 47, 55, 68, 74, 89, 10, 25]
比較対象tempよりoutputの方が小さい場合outputに配列をコピー
3
変数b_idxにカウント
3
変数write_idxにカウント
[33, 47, 55, 68, 74, 89, 10, 25]
[33, 47, 55, 68, 74, 89, 10, 25]
比較対象tempよりoutputの方が小さい場合outputに配列をコピー
4
変数b_idxにカウント
b_yetをfalseにする
4
変数write_idxにカウント
4
span_idx+span_sizeを足してソートする場所を変更
4
a_idxを初期化
6
b_idxを初期化
4
span_sizeの値
4
span_idxの値
[74, 47, 0, 0]
配列tempに比較対象を追加
[74, 89, 0, 0]
配列tempに比較対象を追加
[33, 47, 55, 68, 74, 89, 10, 25]
[33, 47, 55, 68, 10, 89, 10, 25]
比較対象tempよりoutputの方が小さい場合outputに配列をコピー
7
変数b_idxにカウント
5
変数write_idxにカウント
[33, 47, 55, 68, 10, 89, 10, 25]
[33, 47, 55, 68, 10, 25, 10, 25]
比較対象tempよりoutputの方が小さい場合outputに配列をコピー
8
変数b_idxにカウント
b_yetをfalseにする
6
変数write_idxにカウント
[33, 47, 55, 68, 10, 25, 10, 25]
[33, 47, 55, 68, 10, 25, 74, 25]
比較対象tempよりoutputの方が大きい場合outputに配列をコピー
5
変数a_idxにカウント
7
変数write_idxにカウント
[33, 47, 55, 68, 10, 25, 74, 25]
[33, 47, 55, 68, 10, 25, 74, 89]
比較対象tempよりoutputの方が大きい場合outputに配列をコピー
6
変数a_idxにカウント
a_yetをfalseにする
8
変数write_idxにカウント
8
span_idx+span_sizeを足してソートする場所を変更
8
span_size自身を*2して次の分割地点に移動
0
a_idxを初期化
4
b_idxを初期化
8
span_sizeの値
0
span_idxの値
[33, 89, 0, 0]
配列tempに比較対象を追加
[33, 47, 0, 0]
配列tempに比較対象を追加
[33, 47, 55, 0]
配列tempに比較対象を追加
[33, 47, 55, 68]
配列tempに比較対象を追加
[33, 47, 55, 68, 10, 25, 74, 89]
[10, 47, 55, 68, 10, 25, 74, 89]
比較対象tempよりoutputの方が小さい場合outputに配列をコピー
5
変数b_idxにカウント
1
変数write_idxにカウント
[10, 47, 55, 68, 10, 25, 74, 89]
[10, 25, 55, 68, 10, 25, 74, 89]
比較対象tempよりoutputの方が小さい場合outputに配列をコピー
6
変数b_idxにカウント
2
変数write_idxにカウント
[10, 25, 55, 68, 10, 25, 74, 89]
[10, 25, 33, 68, 10, 25, 74, 89]
比較対象tempよりoutputの方が大きい場合outputに配列をコピー
1
変数a_idxにカウント
3
変数write_idxにカウント
[10, 25, 33, 68, 10, 25, 74, 89]
[10, 25, 33, 47, 10, 25, 74, 89]
比較対象tempよりoutputの方が大きい場合outputに配列をコピー
2
変数a_idxにカウント
4
変数write_idxにカウント
[10, 25, 33, 47, 10, 25, 74, 89]
[10, 25, 33, 47, 55, 25, 74, 89]
比較対象tempよりoutputの方が大きい場合outputに配列をコピー
3
変数a_idxにカウント
5
変数write_idxにカウント
[10, 25, 33, 47, 55, 25, 74, 89]
[10, 25, 33, 47, 55, 68, 74, 89]
比較対象tempよりoutputの方が大きい場合outputに配列をコピー
4
変数a_idxにカウント
a_yetをfalseにする
6
変数write_idxにカウント
[10, 25, 33, 47, 55, 68, 74, 89]
[10, 25, 33, 47, 55, 68, 74, 89]
比較対象tempよりoutputの方が小さい場合outputに配列をコピー
7
変数b_idxにカウント
7
変数write_idxにカウント
[10, 25, 33, 47, 55, 68, 74, 89]
[10, 25, 33, 47, 55, 68, 74, 89]
比較対象tempよりoutputの方が小さい場合outputに配列をコピー
8
変数b_idxにカウント
b_yetをfalseにする
8
変数write_idxにカウント
8
span_idx+span_sizeを足してソートする場所を変更
16
span_size自身を*2して次の分割地点に移動
[10, 25, 33, 47, 55, 68, 74, 89]

"""###########################################################################
