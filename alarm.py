import time
import winsound
print("Made by SabiTeach")

def myAlarm():
    try:
        myTime = list(map(int, input("Enter time in hr min sec\n").split()))
        if len(myTime) ==3:
            total_seconds=myTime[0]*60*60+myTime[1]*60+myTime[2]
            time.sleep(total_seconds)

            frequency=2500 #set frequency to 2500 Hertz
            duration=1000 #set duration to 1000 ms = 1sec
            winsound.Beep(frequency, duration)
        else:
            print("Please enter time in correct format as mentioned\n use spaces to differentiate")
            myAlarm()
    except Exception as e:
        print("This is the exception\n", e,"So!, please enter the correct details")
        myAlarm()
myAlarm()