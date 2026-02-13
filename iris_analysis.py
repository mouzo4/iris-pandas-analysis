"""
Iris Dataset Analysis
Assignment 3
Author: Mazen Mahmoud
"""

import pandas as pd

try:
    # Load the two datasets
    petal = pd.read_csv("Petal_Data.csv")
    sepal = pd.read_csv("Sepal_Data.csv")

    # Combine them into one DataFrame
    iris = pd.merge(petal, sepal, on=["sample_id", "species"])

    print("Data combined successfully.\n")

    # Correlation
    print("Correlation Matrix:")
    print(iris.corr(numeric_only=True))
    print()

    # Mean
    print("Average Values:")
    print(iris.mean(numeric_only=True))
    print()

    # Median
    print("Median Values:")
    print(iris.median(numeric_only=True))
    print()

    # Standard Deviation
    print("Standard Deviation:")
    print(iris.std(numeric_only=True))
    print()

    # Species comparison
    print("Species Comparison:")
    print(iris.groupby("species").mean(numeric_only=True))

except FileNotFoundError:
    print("Error: One of the CSV files was not found.")
except Exception as e:
    print("Unexpected error:", e)
