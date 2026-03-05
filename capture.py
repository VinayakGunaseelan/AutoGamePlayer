import mss
import numpy as np
import cv2
import time
import pytesseract

def capturing():

    with mss.mss() as sct:

        if len(sct.monitors) >= 1:
            print(f"Number of monitors{len(sct.monitors)}")
  
        screenshot = sct.grab(sct._monitors[1]) # takes a screenshot of my extended monitor

        frame = np.array(screenshot) # converting the screenshot into an array
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY) # conversion to in gray allowing tesseract can read
        text = pytesseract.image_to_string(frame_gray)
        print(f"Text detected: {text[:50]}...")

        if 'Successful' in text or 'Failure' in text:
            if 'Successful' in text:
                return 'Success'
            else:
                return 'Failure'
            
        return False
        

def screenshot():
    time.sleep(5)
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])
        frame = np.array(screenshot)
        cropped = frame[420:445, 1012:1095]
        cv2.imwrite('targets/failure.png', cropped)
        print('image saved')