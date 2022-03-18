from alarm_clock import AlarmClock

# As a developer, I want to import the AlarmClock class into main.py so I can instantiate it as a new AlarmClock object and call methods on it.

# 1. Print the clock’s time to the terminal

# 2. Call the alarm clock’s change current time method to change the current time

# 3. Toggle the alarm clock’s on off switch




morning_alarm= AlarmClock("My morning alarm")
print (morning_alarm.is_on)

time_is = AlarmClock("1030")
print (time_is.time) 

new_time_is = AlarmClock("1202")
print (new_time_is.change_time)

toggle_on_off = AlarmClock("on")
print (toggle_on_off.is_on)