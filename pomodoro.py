from plyer import notification
import sys



import winsound
import time

# Play a beep sound



# Title and message for the notification
title = 'Pomodoro time!'
message = 'It\'s time to take a 10 min break!'



title2 = 'Break Time Over'
message2 = 'Time to get back to work!'



# Sending the notification

while True == True:
  time.sleep(1500)
  winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
  notification.notify(title=title, message=message, timeout=10)



  time.sleep(600)
  winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
  notification.notify(title=title2, message=message2, timeout=10)




