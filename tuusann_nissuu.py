
#うるう年含めての通算日数の求め方
AD = 1999
now_AD = 2019
Total_days= 0

month = 5
day = 27

t =[31,28,31,30,31,30,31,31,30,31,30,31]
K = [31,29,31,30,31,30,31,31,30,31,30,31]

now_month = 8
now_day = 10


def syori(b):
    Total_day2 =0
    Total_day3 =0
    if b == 0:
        for i in range(month-1):
            Total_day2 = Total_day2 + K[i]
        Total_day2 = Total_day2 + day
        for i in range(now_month-1):
            Total_day3 = Total_day3 + K[i]
        Total_day3 = Total_day3 + now_day
        a = Total_day3 - Total_day2
    else:
        for i in range(month-1):
            Total_day2 = Total_day2 + t[i]
        Total_day2 = Total_day2 + day
        for i in range(now_month-1):
            Total_day3 = Total_day3 + t[i]
        Total_day3 = Total_day3 + now_day
        a = Total_day3 - Total_day2
    return a+Total_days

for i in range(1,now_AD-AD+1):
    num = AD+i
    if num % 400 == 0 or num % 4 == 0:
        Total_days = Total_days + 366
    else:
        Total_days = Total_days + 365

if num % 400 == 0 or num% 4 ==0:
    pp = syori(0)
else:
    pp = syori(1)

print(pp)

#
