# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 15:26:44 2023

@author: Camilo.Munoz
"""

import pandas as pd
import os

# Set the directory where the CSV files are located
directory = r'C:\Users\camilo.munoz\Documents\Data_Extractions\Antofagasta\Jan_2024'

# Get a list of all CSV files in the directory
csv_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')]

# Create an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Loop through each CSV file and append its data to the combined DataFrame
for file in csv_files:
    # Read the CSV file into a DataFrame
    data = pd.read_csv(file)
    
    # Rename the 'Presion' column to match the file name
    data = data.rename(columns={'P21': os.path.basename(file).split(' - ')[0]})

    # Set the index to the columns we want to group by
    data = data.set_index(['Mes', 'Dia', 'Hora'])
    
    # Append the data to the combined DataFrame
    combined_data = pd.concat([combined_data, data], axis=1)

# Reset the index to make the columns into regular columns
combined_data = combined_data.reset_index()

# Save the combined data to a new CSV file
combined_data.to_csv(r'C:\Users\camilo.munoz\Documents\Data_Extractions\Antofagasta\Jan_2024\Unida.csv', index=False)

# Read the CSV file
df = pd.read_csv('Unida.csv')

# Replace NULL values with -1
df.fillna(-1, inplace=True)

# Save the new CSV file
df.to_csv('Reporte_Antofagasta_Procesado_2.csv', index=False)

# read the CSV file
df = pd.read_csv('Reporte_Antofagasta_Procesado_2.csv')

# Get the list of column names
cols = df.columns.tolist()

# Remove columns that don't have ".csv" in their names, except for "Mes", "Dia", and "Hora"
for col in cols:
    if '.csv' not in col and col not in ["Mes", "Dia", "Hora"]:
        df.drop(col, axis=1, inplace=True)
        
# save the updated CSV file
df.to_csv('Reporte_Antofagasta_Limpio.csv', index=False)