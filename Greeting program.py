import time
Current_time = time.localtime()
Current_hour =Current_time.tm_hour
if Current_hour <12 and Current_hour >=5:
    print("Good Morning")
elif Current_hour <16:
    print("Good Afternoon")
elif Current_hour <21:
    print("Good Evening")
else:    print("Good Night")