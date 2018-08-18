from datetime import date, timedelta

d1 = date(2018, 8, 16)  # start date
d2 = date(2018, 8, 30)  # end date

delta = d2 - d1         # timedelta

for i in range(delta.days + 1):
 	x = str(d1 + timedelta(i))
 	x = x.replace('-',',')
 	y = x.split(',')
 	year = int(y[0])
 	month = int(y[1])
 	day = int(y[2])
    selected_weekday = 3  # selected weekday
 	check_day = date(year,month,day)
 	if check_day.weekday() == selected_weekday:
 		print(check_day)


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
