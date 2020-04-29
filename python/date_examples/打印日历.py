import calendar

year = int(input('the year you want to print:'))
year_calendar_str = calendar.calendar(year)
print(f'{year}年的日历图：{year_calendar_str}\n')
