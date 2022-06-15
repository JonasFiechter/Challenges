'''
Return the Time Saved by Speeding
One cause for speeding is the desire to shorten the time spent traveling. In 
long distance trips, speeding does save an appreciable amount of time. However, 
the same cannot be said about short distance trips.

Create a function that calculates the amount of time saved were you traveling 
with an average speed that is above the speed-limit as compared to traveling 
with an average speed exactly at the speed-limit.

Examples
# The parameter's format is as follows:
# (speed limit, avg speed, distance traveled at avg speed)

time_saved(80, 90, 40) ➞ 3.3

time_saved(80, 90, 4000) ➞ 333.3

time_saved(80, 100, 40 ) ➞ 6.0

time_saved(80, 100, 10) ➞ 1.5
Notes
Speed = distance/time
The time returned should be in minutes, not hours.
Round the answer to one decimal place.
The speed limit and average speed are both given in mi/hr
'''


def time_saved(speed_limit, avg_speed, distance_traveled):
    return round((distance_traveled / speed_limit * 60) - (distance_traveled / avg_speed * 60), 1)


print(time_saved(80, 90, 40))
print(time_saved(80, 90, 4000))
print(time_saved(80, 100, 40 ))