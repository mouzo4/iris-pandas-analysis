# Iris Pandas Analysis

# Purpose

This project analyzes the Iris dataset using Python and Pandas.
The goal is to combine petal and sepal data into one DataFrame
and perform statistical analysis.

# What This Program Does

1. Loads Petal_Data.csv and Sepal_Data.csv
2. Combines them into one DataFrame
3. Calculates correlation between variables
4. Calculates mean of each measurement
5. Calculates median of each measurement
6. Calculates standard deviation
7. Compares species to see which are most similar

# Files in This Repository

- Petal_Data.csv
- Sepal_Data.csv
- iris_analysis.py
- README.md

# How to Run

Make sure Python and Pandas are installed.

Run:

python iris_analysis.py

# Design Explanation

The program uses Pandas to:
- Load CSV files
- Merge them using sample_id and species
- Perform statistical calculations
- Group by species to compare similarities

Error handling is included to prevent crashes if files are missing.

# Limitations

- The program assumes the CSV files are formatted correctly.
- It does not clean or modify the dataset.

