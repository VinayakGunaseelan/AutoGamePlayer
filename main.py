import pyautogui as pa
import time
import pandas as pd
import random
from capture import capturing

def main():

    print('go to game window pls')
    time.sleep(10 + random.uniform(-0.5, 0.5))xc

    df = pd.read_csv("cursed_techniques.csv")

    sorted_df = df.sort_values(by='DPS', ascending=False)
    
    try:
        cycle_count = 0
        while True:
            result = capturing()

            if result:
                print(f"Raid Complete {result}, Total Cycles Needed: {cycle_count}")
                break

            else:
                print("Continuing cycle")
    
                for index, row in sorted_df.iterrows():  # iterrows must have (), index is the row number
                    pa.press(row['Key']) # row is the actual data here
                    time.sleep(row['Duration/s']+random.uniform(-0.15, 1)) # added +1 incase time doesnt match its time.sleep not pa.sleep

                    result = capturing()
                    if result:
                        print(f"Raid Complete: {result}, Total Cycles Needed: {cycle_count}")
                        break # if it actually breaks, will also skip the last else and just break
                    else:
                        print("Continuing cycle")
                
                else:
                    cycle_count += 1
                    print(f'Cycle {cycle_count} complete, continuing...')
                    continue
                
                break

    except KeyboardInterrupt:
        print(f"\nStopped manually after {cycle_count}.")
        

if __name__ == "__main__":
    main()