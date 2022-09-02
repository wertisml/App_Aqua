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
start.loc[~(start['Feet H2O'] > 0), 'Feet H2O']=np.nan

#Deletes the 2 old columns
start.drop(start.columns[11], axis=1) #notes
start.drop(start.columns[2], axis=1) #Time
start.drop(start.columns[1], axis=1) #Date
#STREAM NAME CALL
#Choose the one you want and it will name the whole column
#start['Stream Name'] = 'Boone Creek'
#start['Stream Name'] = 'East Fork'
#start['Stream Name'] = 'Flannery Fork'
#start['Stream Name'] = 'Goshen Creek'
#start['Stream Name'] = 'Hodges Creek'
#start['Stream Name'] = 'Middle Fork'
#start['Stream Name'] = 'State farm'
#start['Stream Name'] = 'Winkler Creek'

#create a blank ET column
#start['ET'] = ""
#Reorders the columns
start = start[['Stream ID', 'Date/Time', 'ET (min)','Temp (F)', 'Feet H2O', 'Inches Hg',
               'Volts', ' pH', 'microSiemens/cm Specific Conductivity']]
#Changes the name of columns to match what will be uploaded
start = start.rename(columns={'Stream ID': 'Stream Name', 'Date/Time': 'DATE TIME',
                              'ET (min)': 'ET', 'Temp (F)': 'Temp', 'Feet H2O': 'Pressure',
                              'Inches Hg': 'Barometric', 'Volts': 'Battery',
                              'microSiemens/cm Specific Conductivity': 'Conductivity' })
#all that needs to be done is manually reviewing and adding the ET column
#Best method for ET is on the first row have =0 then the next is =15+(row loaction that is 0) then drag 
#that column down to when the next calimration happened, then repeat the process.



start.to_excel('C:\\Users\\owner\\Documents\\AppAqua\\AppAqua\\2010\\Edited_data\\Boone_Creek\\Boone_Creek16.xlsx', index = False, header = True)

