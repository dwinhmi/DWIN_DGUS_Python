# DWIN Demo code for Raspberry PI
import dwin as HMI
import time
from datetime import datetime
import os
import sys


HMI.pageSwitch(3) # to change to page no 3
HMI.hmiBrightness(50)  # To set Brightness 50

​
try:
    while True:
        # Run your logic here
​
except KeyboardInterrupt:
    pass
# end