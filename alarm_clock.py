

# As a developer, I want to use Python’s proper snake_case for variable names.

# As a developer, I want to create a AlarmClock class.

# As a developer, I want the AlarmClock class to have class instance variables to keep track of the AlarmClock’s current time, whether the alarm is on or off,
#  and the time the alarm is set to. (You can use arbitrary strings to represent the time, it does not need to accurately tell the current time or change over
#  time).

# As a developer, I want the AlarmClock class to have a method to set (or change) the current time and print to the console the current time.

# As a developer, I want the AlarmClock class to have a method to toggle the alarm on or off.

# As a developer, I want the AlarmClock class to have a method to set the current alarm time and print to the console the current alarm time.

# As a developer, I want to import the AlarmClock class into main.py so I can instantiate it as a new AlarmClock object and call methods on it.

# 1. Print the clock’s time to the terminal

# 2. Call the alarm clock’s change current time method to change the current time

# 3. Toggle the alarm clock’s on off switch




class AlarmClock: 
    def __init__(self, name):
        self.alarm = ""
        self.name = name
        self.is_on = True
        self.time = ""
        self.change_time = ""
        pass
        
        

    def alarm_name(self):
        self.name = input ("Please name your alarm.:  ")
        print ("Alarm name is: ", self.name)
        pass
   
    def set_time(self):
        self.time = input ("Please set the time.:  ")
        print ("The current time is set to: ", self.time)
        pass
  
    def new_time(self):
        self.change_time = input ("What time would you like to change it to?:  ")
        print ("The time has been changed to:  ", self.change_time)
        pass
  
    def alarm_on_off(self):
        input("Would you like to turn your alarm on?  ")
        if self.is_on == True:
            print ("Your alarm is on!")
        else:
            print ("Your alarm is off!  ")
        pass
  
    def set_my_alarm(self):
        self.alarm = input("What time would you like to set your alarm to?:  ")
        print("Your alarm is set to:  ", self.alarm)
        pass
