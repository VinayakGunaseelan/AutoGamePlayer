import pyautogui as pa
import time
import pandas as pd

def main():

    print('go to game window pls')
    pa.sleep(10)

    df = pd.read_csv("cursed_techniques.csv")

    sorted_df = df.sort_values(by='DPS', ascending=False)

    for index, row in df.iterrows():  # iterrows must have (), index is the row number
        pa.press(row['Key']) # row is the actual data here
        time.sleep(row['Duration/s']+1) # added +1 incase time doesnt match its time.sleep not pa.sleep
    
    print("Cycle complete")

if __name__ == "__main__":
    main()