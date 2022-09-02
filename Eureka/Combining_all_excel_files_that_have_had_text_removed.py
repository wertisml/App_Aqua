# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 12:16:08 2021

@author: werti
"""

import os
import glob
import pandas as pd

#Working directory, we can change this to what ever folder 
#we are writing the cleaned files into 
os.chdir('C:/Users/owner/Documents/AppAqua/AppAqua/2020/Edited_data')

extension = 'xlsx'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_excel = pd.concat([pd.read_excel(f) for f in all_filenames ])
#export to xlsx
combined_excel.to_excel( "combined_excel.xlsx", index=False, encoding='utf-8-sig')