import pyautogui as pa
import time

# Give some time to switch to the target application
time.sleep(10)

for i in range(1):
    pa.press('x')
    time.sleep(5)
    pa.press('f')
    time.sleep(5)
    pa.press('c')

print('donee')