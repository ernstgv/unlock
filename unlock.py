import pyautogui,time, sys
from datetime import datetime

pyautogui.FAILSAFE = False

while True:

	timestamp = datetime.now()
	
	message = "I ran at " + timestamp.strftime("%d-%b-%Y (%H:%M:%S.%f)")
	
	unlocklog = open("C:/temp/unlock/unlocklog.txt","w")
	
	unlocklog.write(message)
	
	unlocklog.close()

	time.sleep(480)

	pyautogui.press('numlock')

