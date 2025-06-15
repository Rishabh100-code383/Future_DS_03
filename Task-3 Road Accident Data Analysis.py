# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 11:07:04 2025

@author: risha
"""

# Author: Rishabh Gupta
# Task 3: Road Accident Analysis Dashboard (Future Interns - Data Science & Analytics)
# Tools: Python (pandas), Excel

import pandas as pd

# Step 1: Load the dataset
file_path = r"C:\Users\risha\Downloads\Road Accident Data.xlsx"  # update if needed
df = pd.read_excel(file_path)

# Step 2: Basic inspection
print("Initial shape:", df.shape)
print("Column names:\n", df.columns)

# Step 3: Clean column names
df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace(r'[^\w]', '', regex=True)

# Step 4: Check for nulls
print("\nMissing values:\n", df.isnull().sum())

# Step 5: Convert data types if needed
df['Accident_Date'] = pd.to_datetime(df['Accident_Date'], errors='coerce')

# Step 6: Feature engineering
df['Year'] = df['Accident_Date'].dt.year
df['Month'] = df['Accident_Date'].dt.month_name()
df['DayOfWeek'] = df['Accident_Date'].dt.day_name()

# Step 7: Grouping examples
# Total accidents per year
accidents_per_year = df.groupby('Year')['Accident_Index'].nunique().reset_index(name='Total_Accidents')
print("\nAccidents per Year:\n", accidents_per_year)

# Casualties by severity
severity_counts = df['Accident_Severity'].value_counts()
print("\nCasualties by Severity:\n", severity_counts)

# Step 8: Save cleaned data to Excel for Power BI
output_file = 'Road_Accident_Cleaned.xlsx'
df.to_excel(output_file, index=False)
print(f"\n✅ Cleaned data saved as: {output_file}")


# Accidents by Road Type
print(df['Road_Type'].value_counts())

# Urban vs Rural Distribution
print(df['Urban_or_Rural_Area'].value_counts())

# Light condition breakdown
print(df['Light_Conditions'].value_counts())


# Option: Fill missing categorical columns
df['Carriageway_Hazards'].fillna('Unknown', inplace=True)
df['Time'].fillna('Unknown', inplace=True)
