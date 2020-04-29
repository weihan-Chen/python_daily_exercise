import calendar

year = int(input('year:'))
month = int(input('month:'))
month_calendar_str = calendar.month(year, month)

print(f'{year}年-{month}月的日历图：{month_calendar_str}')
