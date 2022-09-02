###Before running this code make sure that the file has the top rows 
#removed until the top row starts with DATE or else this will
#not work and you will get an error

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

start = pd.read_csv(data, sep =',', names = list(["DATE", "TIME", "Temp_deg_F", "Depth_ft", "Int_Batt_V", "pH_units", "SpCond_uS/cm", "HDO_%Sat"]))
#Removing the first row of the file becasue its unneeded
#Removing all rows that start with Date or Eureka becasue those only
#show up when there has been an error in recoding data
start = start.iloc[1: , :]
start.drop(start.index[(start["DATE"] == "DATE")],axis=0,inplace=True)
start.drop(start.index[(start["DATE"] == "Eureka_Manta_2")],axis=0,inplace=True)
#add a line to remove the time stamps for years that we are not looking at
#if the first file contains a different year make sure that gets removed 
#same as at the end of the file

#start.drop(start.index[(start["DATE"] == "change this to the time frame being removed")],axis=0,inplace=True)

rec = pd.DataFrame(start)

rec.to_excel('C:\\Users\\werti\\OneDrive\\Documents\\AppAqua\\2018\\Raw_data\\East_Fork\\cleaned5.xlsx', index = False, header = True)
#how to add new excel files onto the end of existing excel files 
#so that there is one large file that needs to be run instead of a 
#bunch of small ones

