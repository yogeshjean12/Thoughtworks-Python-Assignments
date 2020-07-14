import sys

class Time:
    ''' Time related operations '''
    hours = 24
    minutes = 60

    def __init__(self, first_time, second_time):
        if (first_time[0] <= self.hours and first_time[0] >= 0 ) and (first_time[1] <= self.minutes and first_time[1] >= 0):
            self.first_time = first_time
        else:
            sys.exit('Error in the first time format, Try again with the correct time format')
        if (second_time[0] <= self.hours and second_time[0] >= 0) and (second_time[1] <= self.minutes and second_time[1] >= 0):
            self.second_time = second_time
        else:
            sys.exit('Error in the second time format, Try again with the correct time format')

    def add_time(self):
        hour = self.first_time[0] + self.second_time[0]
        mins = self.first_time[1] + self.second_time[1]
        if mins >= 60:
            mins -= 60
            hour += 1
        return 'Concatenated time is {}hr and {}mins'.format(hour,mins)

    def time_difference(self):
        if self.first_time[0] >= self.second_time[0]:
            hour = self.first_time[0] - self.second_time[0]
        else:
            hour = self.second_time[0] - self.first_time[0]

        if self.first_time[1] >= self.second_time[1]:
            mins = self.first_time[1] - self.second_time[1]
        else:
            mins = self.second_time[1] - self.first_time[1]

        return 'Time difference is {}hr and {}mins'.format(hour,mins)

    def time_in_minutes(self):
        mins = (self.first_time[0]*self.minutes)+(self.second_time[0]*self.minutes)+(self.first_time[1]+self.second_time[1])
        return 'Total time taken in minutes is {}mins'.format(mins)
try:
    print('Use 24 hours time format')
    first_time=list(map(int,input('Enter the first time separated by colon(:) Eg.5:30 : ').strip().split(':')))
    second_time=list(map(int,input('Enter the second time separated by colon(:) Eg.2:15 : ').strip().split(':')))
except Exception:
    print('Wrong input format, Enter the input as specified, Try again with the correct input format')
else:
    Time_1 = Time(first_time, second_time)
    print(Time_1.add_time())
    print(Time_1.time_difference())
    print(Time_1.time_in_minutes())
