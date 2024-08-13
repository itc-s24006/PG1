from datetime import date
day_now = date.today()
print(day_now)

xday = date(2024, 4, 5)
td = day_now - xday
print(f"入学してから{td}")

yday = date(2005, 9, 26)
td = day_now - yday
print(f"生まれてから{td}")
