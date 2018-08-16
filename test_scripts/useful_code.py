# from datetime import date, timedelta, datetime
#
# def month_weekday(year,month,day):
#        dt = date(year, month, day)
#        print('dt: ',dt)
#        while dt.month == month:
#           yield dt
#           dt += timedelta(days = 7)
# now = datetime.now()
# current_year = now.year
# mon = 6
# tue = 7
# wed = 1
# thurs = 2
# fri = 3
# sat = 4
# sun = 5
#
# for s in month_weekday(current_year,8,sun):
#    print(s)

# dropdown menu

# in the view:
#
# def your_handler(request):
#     z = [1, 2, 3, 4]
#     return render(request, 'yourapp/your_template.html', {'z': z})
# in the template:
#
# <label>values in z<label>
# <select id="the-id">
#     {% for i in z %}
#     <option value="{{ i }}">{{ i }}</option>
#     {% endfor %}
# </select>

import datetime
from dateutil import relativedelta

nextmonth = datetime.date.today() + relativedelta.relativedelta(months=1)
nextmonth = nextmonth.strftime("%B")
print(nextmonth)
