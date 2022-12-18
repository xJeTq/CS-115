'''
Created on 11/30/2022 
@author:   Anthony Curcio-Petraccoro 
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. 

CS115 - Hw 12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self): 
        '''Returns a new object with the same month, day, year 
           as the calling object (self).''' 
        dnew = Date(self.month, self.day, self.year) 
        return dnew

    def equals(self, d2): 
        '''Decides if self and d2 represent the same calendar date, 
            whether or not they are the in the same place in memory.''' 
        return self.year == d2.year and self.month == d2.month and self.day == d2.day

    def tomorrow(self):
        '''Properly calculates tomorrow's date; accounting for month, year alterations and leap years.'''
        DIM = (0,31,28,31,30,31,30,31,31,30,31,30,31)
        lastDate = DIM[self.month]
        if self.month != 12:
            if self.month == 2 and self.day == 28 and Date(self.day, self.month, self.year).isLeapYear():
                self.day = 29 
                self.month = 2 
                self.year = self.year
            elif self.day + 1 > lastDate:
                self.day = 1
                self.month = self.month + 1
                self.year = self.year
            else:
                self.day = self.day + 1
                self.month = self.month
                self.year = self.year
        else:
            if self.day == 31:
                self.day = 1
                self.month = 1
                self.year = self.year + 1
            else:
                self.day = self.day + 1
                self.month = 12
                self.year = self.year

    def yesterday(self):
        '''Properly calculates yesterday's date; accounting for month, year alterations and leap years.'''
        DIM = (0,31,28,31,30,31,30,31,31,30,31,30,31)
        if self.month != 1:
            if self.month == 3 and self.day == 1 and Date(self.day, self.month, self.year).isLeapYear():
                self.day = 29
                self.month = self.month - 1
                self.year = self.year
            elif self.day == 1:
                self.day = DIM[self.month - 1]
                self.month = self.month - 1
                self.year = self.year
            else:
                self.day = self.day - 1
                self.month = self.month
                self.year = self.year
        else:
            if self.day == 1:
                self.day = 31
                self.month = 12
                self.year = self.year - 1
            else: 
                self.day = self.day - 1
                self.month = 1
                self.year = self.year

    def addNDays(self, N):
        '''Adds the inputted amount of days to the current date. Properly accounts for days, months, years and leap years.'''
        days = Date(self.month, self.day, self.year)
        #print("Many Days Later...")
        while N > 0:
            print(days)
            days.tomorrow()
            N = N - 1
        print(days)
        self.day = days.day
        self.month = days.month
        self.year = days.year

    def subNDays(self, N):
        '''Subtracts the inputted amount of days to the current date. Properly accounts for days, months, years and leap years.''' 
        days = Date(self.month, self.day, self.year)
        #print("Many Days Later...")
        while N > 0:
            print(days)
            days.yesterday()
            N = N - 1
        print(days)
        self.day = days.day
        self.month = days.month
        self.year = days.year

    def isBefore(self, d2):
        '''Tests to see if a date is before another date inputted.''' 
        day1 = Date(self.month, self.day, self.year)
        day2 = d2
        if day2.year > day1.year:
            return True
        elif day2.year == day1.year and day2.month > day1.month:
            return True
        elif day2.year == day1.year and day2.month == day1.month and day2.day > day1.day:
            return True
        else:
            return False

    def isAfter(self, d2):
        '''Tests to see if a date is after another date inputted.''' 
        day1 = Date(self.month, self.day, self.year)
        day2 = d2
        if day2.year < day1.year:
            return True
        elif day2.year == day1.year and day2.month < day1.month:
            return True
        elif day2.year == day1.year and day2.month == day1.month and day2.day < day1.day:
            return True
        else:
            return False

    def diff(self, d2):
        '''Returns the difference in two dates.'''
        counter = 0
        d1 = Date(self.month, self.day, self.year).copy()
        D2 = d2.copy()
        if d1.isBefore(D2):
            while d1.isBefore(D2):
                counter = counter - 1
                d1.tomorrow()
        else:
            while d1.isAfter(D2):
                d1.yesterday()
                counter = counter + 1
        return counter            
            
    def dow(self):
        '''Calculates the day of the week given any date.'''
        difference = self.diff(Date(12, 4, 2022)) % 7
        if difference == 0:
            return "Sunday"
        elif difference == 1:
            return "Monday"
        elif difference == 2:
            return "Tuesday"
        elif difference == 3:
            return "Wednesday"
        elif difference == 4:
            return "Thursday"
        elif difference == 5:
            return "Friday"
        else:
            return "Saturday"
        
