from datetime import date, timedelta, datetime

def month_weekday(year,month,day):
       dt = date(year, month, day)
       print('dt: ',dt)
       while dt.month == month:
          yield dt
          dt += timedelta(days = 7)
now = datetime.now()
current_year = now.year
mon = 6
tue = 7
wed = 1
thurs = 2
fri = 3
sat = 4
sun = 5

for s in month_weekday(current_year,8,sun):
   print(s)
