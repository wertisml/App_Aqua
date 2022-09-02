import pandas as pd
import glob
import os
os.chdir('C:\\Users\\owner\\Documents\\AppAqua\\AppAqua\\2020\\Raw_data\\Winkler_Creek')

path = r'C:\Users\owner\Documents\AppAqua\AppAqua\2020\Raw_data\Winkler_Creek'
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, sep = ',', names = list(["DATE", "TIME", "Temp_deg_F", "Depth_ft", "Int_Batt_V", "pH_units", "SpCond_uS/cm", "HDO_%Sat"]))
    df = df.iloc[1: , :]
    df.drop(df.index[(df["DATE"] == "DATE")],axis=0,inplace=True)
    df.drop(df.index[(df["DATE"] == "Eureka_Manta_2")],axis=0,inplace=True)

    li.append(df)

    
frame = pd.concat(li, axis=0, ignore_index=True)

frame.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')



#IF you encounter - ValueError: operands could not be broadcast together with shapes (0,) (2,) (0,) 
#Go into the csv and delete column 1 from all the files and it should work