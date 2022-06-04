'''
Friday the 13th
Given the month and year as numbers, return whether that month contains a 
Friday 13th.

Examples
has_friday_13(3, 2020) ➞ True

has_friday_13(10, 2017) ➞ True

has_friday_13(1, 1985) ➞ False
Notes
January will be given as 1, February as 2, etc ...
Check Resources for some helpful tutorials on Python's datetime module.
'''
from calendar import Calendar

weekdays = {
    '0': 'Monday',
    '1': 'Tuesday',
    '2': 'Wednsday',
    '3': 'Tuersday',
    '4': 'Friday',
    '5': 'Saturday',
    '6': 'Sunday',
}

def has_friday_13(month, year):
    cal = Calendar()
    monthdays = cal.monthdatescalendar(year, month)
    for week in monthdays:
        for day in week:
            if day.strftime('%d') == '13' and day.weekday() == 4:
                return True
            print(day.strftime('%d'), weekdays[str(day.weekday())])
    return False


print(has_friday_13(3, 2020))
print(has_friday_13(10, 2017))
print(has_friday_13(1, 1985))