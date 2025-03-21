class Clock:

    def get_position(self, max_hours, mins_passed):
        hours = 0
        totalmins = mins_passed
        while totalmins > 60:
            totalmins = totalmins-60
            hours = hours + 1
        while hours > max_hours:
            hours = hours-max_hours
        return hours, totalmins

