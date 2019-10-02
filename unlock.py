#!/usr/bin/python

import pyautogui,time, sys
from datetime import datetime

pyautogui.FAILSAFE = False



while True:

	timestamp = datetime.now()
	#ranmessage = "I ran at "
	message = "I ran at " + timestamp.strftime("%d-%b-%Y (%H:%M:%S.%f)")
	#print(timestamp)
	unlocklog = open("C:/temp/unlock7logs/unlocklog.txt","w")
	unlocklog.write(message)
	unlocklog.close()

	time.sleep(480)

	pyautogui.press('numlock')


    #print("I kicked in")
