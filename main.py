import pyautogui as pa
import time
import pandas as pd
import random
from capture import capturing

def main():

    print('go to game window pls')
    time.sleep(10 + random.uniform(-0.5, 0.5))

    df = pd.read_csv("cursed_techniques.csv")

    sorted_df = df.sort_values(by='DPS', ascending=False)
    
    try:
        while True:
            result = capturing()

            if result == 'success':
                print("Raid Complete")
                break

            elif result == 'failure':
                print("Raid Failed")
                break

            raid_done = False
            for index, row in sorted_df.iterrows():  # iterrows must have (), index is the row number
                pa.press(row['Key']) # row is the actual data here
                time.sleep(row['Duration/s']+random.uniform(-0.15, 1)) # added +1 incase time doesnt match its time.sleep not pa.sleep

                result = capturing()
                if result:
                    print(f"Raid ended: {result}")
                    raid_done = True
                    break
    
            if raid_done:
                break

    except KeyboardInterrupt:
        print("\nStopped manually.")
        

if __name__ == "__main__":
    main()