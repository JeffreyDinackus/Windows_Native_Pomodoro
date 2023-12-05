from plyer import notification
import sys

import winsound
import time

# Play a beep sound


# Title and message for the notification
title = 'Rest your eyes'
message = 'rest your eyes!'


title2 = 'look back'
message2 = 'work more'

# Sending the notification

while True == True:
  time.sleep(1500)
  winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
  notification.notify(title=title, message=message, timeout=10)



  time.sleep(120)
  winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
  notification.notify(title=title2, message=message2, timeout=10)





