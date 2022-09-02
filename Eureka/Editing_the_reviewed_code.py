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
start = pd.read_excel(data, header = 0)
#Look for all cases when the Depth value is less then 0 and replaces it with blank cells
start.loc[~(start['Depth_ft'] > 0), 'Depth_ft']=np.nan

#Changing the / to - in the date column to make it how it needs to be
start['DATE'] = start['DATE'].str.replace('/','-')
#Combines the DATE and TIME column
start["DATE TIME"] = start["DATE"].astype(str) + " " + start["TIME"]
#Reformats the new column to the style we need
start['DATE TIME'] = pd.to_datetime(start['DATE TIME'])
#Deletes the 2 old columns
del start['DATE']
del start['TIME']
#STREAM NAME CALL
#Choose the one you want and it will name the whole column
#start['Stream Name'] = 'Boone Creek'
#start['Stream Name'] = 'East Fork'
#start['Stream Name'] = 'Flannery Fork'
#start['Stream Name'] = 'Goshen Creek'
#start['Stream Name'] = 'Hodges Creek'
start['Stream Name'] = 'Middle Fork'
#start['Stream Name'] = 'State farm'
#start['Stream Name'] = 'Winkler Creek'

#create a blank ET column
start['ET'] = ""
#Reorders the columns
start = start[['Stream Name', 'DATE TIME', 'ET','Temp_deg_F', 'Depth_ft', 'HDO_%Sat', 'Int_Batt_V', 'pH_units', 'SpCond_uS/cm']]
#Changes the name of columns to match what will be uploaded
start = start.rename(columns={'Temp_deg_F': 'Temp', 'Depth_ft': 'Pressure', 'HDO_%Sat': 'Barometric', 'Int_Batt_V': 'Battery', 'pH_units': 'pH', 'SpCond_uS/cm': 'Conductivity' })
#all that needs to be done is manually reviewing and adding the ET column
#Best method for ET is on the first row have =0 then the next is =15+(row loaction that is 0) then drag 
#that column down to when the next calimration happened, then repeat the process.



start.to_excel('C:\\Users\\owner\\Documents\\AppAqua\\AppAqua\\2022\\Edited_data\\edited_Middle_Fork.xlsx', index = False, header = True)

