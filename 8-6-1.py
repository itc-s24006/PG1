from datetime import datetime
now = datetime.today()
print(now)              #現在年月日時分秒マイクロ秒
print(now.year)         #現在年
print(now.month)        #現在月
print(now.day)          #現在日
print(now.hour)         #現在時
print(now.minute)       #現在分
print(now.second)       #現在秒
print(now.microsecond)  #現在マイクロ秒

mukasi = datetime(1918, 8, 13, hour=14, minute=56, second=15, microsecond=0)
print(mukasi)

dt = datetime.strptime("13/8/2024 15:15", "%d/%m/%Y %H:%M")
print(dt)

dt2 = dt.strftime("%Y年%m月%d日 %H時%M分")
print(dt2)

