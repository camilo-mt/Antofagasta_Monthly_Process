# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 08:40:30 2023

@author: Camilo.Munoz
"""

import os
import pandas as pd

# Set the directory path where the CSV files are located
directory = r'C:\Users\camilo.munoz\Documents\Data_Extractions\Antofagasta\Nov_2023'

# Loop through all the CSV files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(os.path.join(directory, filename))
        
        
        df = df[~df['Mes'].astype(str).str.startswith(('10', '12'))]
      
        # Save the new DataFrame to a new CSV file with "_new" added to the filename
        new_filename = os.path.splitext(filename)[0] + '_new.csv'
        df.to_csv(os.path.join(directory, new_filename), index=False)