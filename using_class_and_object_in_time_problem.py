import sys

class Time:
    ''' Time '''
    valid_hours = 24
    valid_minutes = 60

    def __init__(self, time):
        if (time[0] <= self.valid_hours and time[0] >= 0 ) and (time[1] <= self.valid_minutes and time[1] >= 0):
            self.hour = time[0]
            self.mins = time[1]
            self.time_in_minutes =self.hour*self.valid_minutes + self.mins
        else:
            sys.exit('Error in the time format, Try again with the correct time format')

def add_time(t1,t2):
        hour = t1.hour + t2.hour
        mins = t1.mins + t2.mins
        if mins >= 60:
            mins -= 60
            hour += 1
        return 'Concatenated time is {}hr and {}mins'.format(hour,mins)

def total_time_in_minutes(t1,t2):
    return 'Total time taken is {}minutes'.format(t1.time_in_minutes + t2.time_in_minutes)

def time_difference(t1, t2):
        if t1.hour >= t2.hour:
            hour = t1.hour - t2.hour
        else:
            hour = t2.hour - t1.hour

        if t1.mins >= t2.mins:
            mins = t1.mins - t2.mins
        else:
            mins = t2.mins - t1.mins

        return 'Time difference is {}hr and {}mins'.format(hour,mins)

try:
    print('Use 24 hours time format')
    t1 = Time(list(map(int,input('Enter the first time separated by colon(:) Eg.5:30 : ').strip().split(':'))))
    t2 = Time(list(map(int,input('Enter the first time separated by colon(:) Eg.5:30 : ').strip().split(':'))))

except Exception:
    print('Wrong input format, Enter the input as specified, Try again with the correct input format')
else:
    print(add_time(t1, t2))
    print(total_time_in_minutes(t1, t2))
    print(time_difference(t1, t2))
