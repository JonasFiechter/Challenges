'''
When to Sleep?
Given a series of lists, with each individual list containing the time of the 
alarm set and the sleep duration, return what time to sleep.

Examples
bed_time(["07:50", "07:50"]) ➞ ["00:00"]
# The second argument means 7 hours, 50 minutes sleep duration.

bed_time(
    ["06:15", "10:00"], 
    ["08:00", "10:00"], 
    ["09:30", "10:00"]
) ➞ ["20:15", "22:00", "23:30"]

# The second argument of each sub list means 10 hours sleep duration.

bed_time(["05:45", "04:00"], ["07:10", "04:30"]) ➞ ["01:45", "02:40"]
# Sleep duration can be different among the lists.
Notes
Times should be given in 24-hrs (i.e. "23:25" as opposed to "11:25PM").
Return a list of strings.
'''

def bed_time(*args):
    result = []
    hours_24 = [hour for hour in range(24)]

    for list in args:
        alarm, amount = list
        result.append(str(hours_24[hours_24.index(int(alarm[0:2])) - int(amount[0:2])]) + f':{alarm[3:]}')

    return result

print(bed_time(
    ["06:15", "10:00"], 
    ["08:00", "10:00"], 
    ["09:30", "10:00"]
))