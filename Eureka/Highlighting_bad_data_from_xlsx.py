import pandas as pd
import csv
import numpy as np
import openpyxl
from  tkinter import *
from tkinter import filedialog
#getting the csv we want to run
root = Tk()

root.filename =  filedialog.askopenfilename(initialdir = "/", title = "Select file")

root.mainloop()


data = root.filename
#is there a difference between a xlsx and csv? could be why its not working
start = pd.read_csv(data, sep =',', header = 0)

#makes sure that each column is numeric becasue sometimes the columns are 
#turned into strings in the csv
df['Depth_ft'] = pd.to_numeric(df.Depth_ft)
df['Int_Batt_V'] = pd.to_numeric(df.Int_Batt_V)
#df['SpCond_uS/cm'] = pd.to_numeric(df.SpCond_uS/cm)
df['pH_units'] = pd.to_numeric(df.pH_units)
#df['HDO_%Sat'] = pd.to_numeric(df.HDO_%Sat)

df = pd.DataFrame(start)

pH_min = 6
pH_max = 9
HDO_Min = 40
Sp_Con = 400
battery = 0
depth = -.01

#shades the column cells based on if they pass or not
rec = df.style\
        .applymap(lambda x: 'background-color: %s' % 'yellow' if x < depth else 'background-color: %s' % 'white', subset=['Depth_ft'])\
        .applymap(lambda x: 'background-color: %s' % 'red' if x <= battery else 'background-color: %s' % 'white', subset=['Int_Batt_V'])\
        .applymap(lambda x: 'background-color: %s' % 'blue' if x > Sp_Con else 'background-color: %s' % 'white', subset=['SpCond_uS/cm'])\
        .applymap(lambda x: 'background-color: %s' % 'orange' if x > pH_max or x < pH_min else 'background-color: %s' % 'white', subset=['pH_units'])\
        .applymap(lambda x: 'background-color: %s' % 'green' if x < HDO_Min else 'background-color: %s' % 'white', subset=['HDO_%Sat'])\




reviewed.to_excel('C:\\Users\\owner\\Documents\\AppAqua\AppAqua\\2020\\Reviewed_data\\reviewed_Boone_Creek.xlsx', index = False, header = True)

#is there a differnce in a dataframe when you read in a csv vs xlsx
#figure out how to save as a csv but also continue to add new csv files onto the bottom of the existing so its all 1 file        
#rec.to_csv('reviewed.csv', index=False)