import pyautogui as pa
import time
import pandas as pd

def main():

    print('go to game window pls')
    pa.sleep(10)

    df = pd.read_csv("cursed_techniques.csv")

    sorted_df = df.sort_values(by='DPS', ascending=False)

    for index, row in df.iterrows():
        pa.press(row['Key'])
        time.sleep(row['Duration/s']+1)
    
    print("Cycle complete")

if __name__ == "__main__":
    main()