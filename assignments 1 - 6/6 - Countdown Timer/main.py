import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs) # Formats the time in the format of mm:ss
        print(timer, end='\r') # Overwrites the same line
        time.sleep(1)
        t -= 1
    
    print('Time is up!')


t = int(input("\nEnter the time in seconds: "))

countdown(t)