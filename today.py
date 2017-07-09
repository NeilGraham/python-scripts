import datetime

now = datetime.datetime.now()

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

day_suffix = 'th'
if now.day <= 3 or now.day >= 21:
    if now.day % 10 == 1 and (now.day <= 3 or now.day >= 20):
        day_suffix = 'st'
    elif now.day % 10 == 2:
        day_suffix = 'nd'
    elif now.day % 10 == 3:
        day_suffix = 'rd'

print('Today is ' + weekday[now.weekday()] + ', ' + month[now.month - 1] + ' ' + str(now.day) + day_suffix + ', ' + str(now.year))



hour_suffix = 'AM'
hour = now.hour
if hour >= 12 and hour <= 23:
	hour_suffix = 'PM'
if hour > 12:
    hour = hour - 12

min_suffix = 's'
if now.minute == 1:
    min_suffix = ''

sec_suffix = 's'
if now.second == 1:
    sec_suffix = ''

if now.minute == 0:
    if now.second == 0:
        print('It\'s currently ' + str(hour) + ' ' + hour_suffix + ' on the dot')
    else:
        print('It\'s ' + str(now.second) + ' second' +  + ' after ' + str(hour) + ' ' + hour_suffix)
elif now.minute == 59:
    print('It\'s ' + str(60 - now.second) + ' second' + sec_suffix + ' before ' + str(hour + 1) + ' ' + hour_suffix)
elif now.minute >= 50:
    if now.second >= 45:
        print('It\'s ' + str(60 - now.minute - 1) + ' minute' + min_suffix + ' and ' + str(60 - now.second) + ' second' + sec_suffix + ' before ' + str(hour + 1) + ' ' + hour_suffix)
    else:
        print('It\'s ' + str(60 - now.minute) + ' minute' + min_suffix + ' before ' + str(hour + 1) + ' ' + hour_suffix)
elif now.minute <= 10:
    if now.second <= 15:
        print('It\'s ' + str(now.minute) + ' minute' + min_suffix + ' and ' + str(now.second) + ' second' + sec_suffix + ' after ' + str(hour + 1) + ' ' + hour_suffix)
    else:
        print('It\'s ' + str(now.minute) + ' minute' + min_suffix + ' after ' + str(hour) + ' ' + hour_suffix)
elif now.minute == 30:
    if now.second == 0:
        print('It\'s ' + str(hour) + ' ' + hour_suffix + ' on the dot')
    else:
        print('It\'s ' + str(now.second) + ' second' +  + ' after ' + str(hour) + ' ' + hour_suffix)
else:
    print('It\'s currently ' + str(hour) + ':' + str(now.minute) + ' ' + hour_suffix)
