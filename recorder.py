import pynput
import mss
from pynput import keyboard
import time
import cv2
import os
import numpy as np

def recording(stop):
    folder_count = sum(1 for entry in os.scandir('Data') if entry.is_dir())
    os.mkdir(f'Data/Set{folder_count}')
    with mss.mss() as sct:
        frame_count = 1
        while not stop.is_set():
            screenshot = sct.grab(sct._monitors[1])
            pixels = np.array(screenshot)
            cv2.imwrite(f'Data/Set{folder_count}/frame{frame_count}.png', pixels)
            frame_count += 1
            time.sleep(0.033)