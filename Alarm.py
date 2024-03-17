
###COMPLETED###

import time

print('Now time:', time.strftime('%H' + ':' + '%M' + ':' + '%S')) #Printing current Time

alarm = input('Enter your alarm time(H:M:S) :') #Alaways input time in H:M:S ex: 21:09:22

while True: #Infinite loop
    tm = time.strftime('%H' + ':' + '%M' + ':' + '%S') # Getting current time
    time.sleep(1) #Very Very IMPORTANT
    #print(tm) #FOR DEVELOPMENT PURPOSE
    if tm == alarm: #If time is alarm time break
        break

print('Alarm executed Time:', alarm) #JUST NOTHING