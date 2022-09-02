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
#need to mess around and make sure I can do this with .csv and not jsut xlsx
start = pd.read_csv(data, sep = ',',  header = 0)

df = pd.DataFrame(start)
#makes sure that each column is numeric becasue sometimes the columns are 
#turned into strings in the csv
df['Depth_ft'] = pd.to_numeric(df.Depth_ft)
df['Int_Batt_V'] = pd.to_numeric(df.Int_Batt_V)
#df['SpCond_uS/cm'] = pd.to_numeric(df.SpCond_uS/cm)
df['pH_units'] = pd.to_numeric(df.pH_units)
#df['HDO_%Sat'] = pd.to_numeric(df.HDO_%Sat)

pH_min = 6
pH_max = 9
HDO_Min = 40
Sp_Con = 400
battery = 0
depth = 0

#shades the column cells based on if they pass or not   #check about changing the white to blank on the depth to delete here instead of later becasue this is more accurate then what im doing later on
rec = df.style\
        .applymap(lambda x: 'background-color: %s' % 'black' if x < depth else 'background-color: %s' % 'white', subset=['Depth_ft'])\
        .applymap(lambda x: 'background-color: %s' % 'red' if x <= battery else 'background-color: %s' % 'white', subset=['Int_Batt_V'])\
        .applymap(lambda x: 'background-color: %s' % 'blue' if x > Sp_Con else 'background-color: %s' % 'white', subset=['SpCond_uS/cm'])\
        .applymap(lambda x: 'background-color: %s' % 'orange' if x > pH_max or x < pH_min else 'background-color: %s' % 'white', subset=['pH_units'])\
        .applymap(lambda x: 'background-color: %s' % 'green' if x < HDO_Min else 'background-color: %s' % 'white', subset=['HDO_%Sat'])\



rec.to_excel('C:\\Users\\owner\\Documents\\AppAqua\\AppAqua\\2022\\Reviewed_data\\reviewed_Middle_Fork.xlsx', index = False, header = True)

