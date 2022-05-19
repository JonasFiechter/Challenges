def convert_to_seconds(minutes=0):
    seconds = minutes * 60
    return

def convert_to_miliseconds(seconds=0):
    miliseconds = seconds * 60
    print('inside convert_to_miliseconds', miliseconds)


minutes_to_test = [5, 12, 5, 6, 7, 8, 2, 1, 2 ,4]
for minutes in minutes_to_test:
    print(minutes, convert_to_miliseconds(seconds=convert_to_seconds(minutes=minutes)))