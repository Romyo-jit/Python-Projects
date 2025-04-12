import time
tm=int(time.strftime('%H'))
if (tm>=18 or tm<4):
     print('Good Night.')
elif (tm>=4 or tm<12):
	    print('Good Morning.')
elif (tm>=12 or tm<18):
	    print('Good Afternoon.')
else:
     print('Time module error can\' find valid time..')