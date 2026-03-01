import mss
import numpy as np
import cv2
import time
import random 

def capturing():

    success = cv2.imread("targets/successful.png") # Imread is used to comvert the image to pixels
    failure = cv2.imread("targets/failure.png")
    
    '''normalized cross-correlation that calculates how much two images "overlap" in pattern 
    while ignoring differences in overall brightness or lighting.
    '''
    with mss.mss() as sct:

        if len(sct.monitors) <= 2:
            print(f"Number of monitors{len(sct.monitors)}")
  
        screenshot = sct.grab(sct._monitors[1]) # takes a screenshot of my extended monitor

        frame = np.array(screenshot) # converting the screenshot into an array
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR) # conversion of frame to grayscale

        result_success = cv2.matchTemplate(frame_gray, success, cv2.TM_CCOEFF_NORMED)
        result_failed = cv2.matchTemplate(frame_gray, failure, cv2.TM_CCOEFF_NORMED)

        print(f"success confidence: {np.max(result_success)}")
        print(f"failure confidence: {np.max(result_failed)}")
        

        threshold = 0.8
        
        # to check whether the raid has actually completed or not
        if np.max(result_success) >= threshold or np.max(result_failed) >= threshold:
            start = time.time()
            while time.time() - start < 3:
                time.sleep(random.uniform(0.8, 1.2)) # essentially pauses the loop every 1 second
                screenshot = sct.grab(sct.monitors[1])
                frame = np.array(screenshot)
                frame_bgr = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

                #np.max is used and it gives max value from matchTemplate

                rs = np.max(cv2.matchTemplate(frame_bgr, success, cv2.TM_CCOEFF_NORMED)) 
                rf = np.max(cv2.matchTemplate(frame_bgr, failure, cv2.TM_CCOEFF_NORMED))

                if rs < threshold and rf < threshold:
                    print('False alarm, continue cycle')
                    return False
                
            if np.max(result_success) >= np.max(result_failed):
                return 'success'
            else:
                return 'failure'
        
        print('continuing cycle')
        return False
            

        

def screenshot():
    time.sleep(5)
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])
        frame = np.array(screenshot)
        cropped = frame[420:445, 1012:1095]
        cv2.imwrite('targets/failure.png', cropped)
        print('image saved')