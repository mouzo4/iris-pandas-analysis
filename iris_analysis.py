"""
Iris Dataset Analysis using Pandas
Assignment 3
Author: Mazen Mahmoud

This script combines petal and sepal data
and performs statistical analysis on the Iris dataset.
"""

import pandas as pd

try:
    # Load datasets
    petal = pd.read_csv("Petal_Data.csv")
    sepal = pd.read_csv("Sepal_Data.csv")

    # Merge datasets on sample_id and species
    iris = pd.merge(petal, sepal, on=["sample_id", "species"])

    print("Data combined successfully.\n")

    # Correlation Analysis 
    # There are 4 numeric variables
    # petal_length, petal_width, sepal_length, sepal_width
    # 4 variables create 6 unique pairwise correlations
    print("Correlation Matrix:")
    correlation_matrix = iris.corr(numeric_only=True)
    print(correlation_matrix)
    print()

    # Mean Calculation 
    print("Average Values:")
    print(iris.mean(numeric_only=True))
    print()

    # Median Calculation 
    print("Median Values:")
    print(iris.median(numeric_only=True))
    print()

    # Standard Deviation
    print("Standard Deviation:")
    print(iris.std(numeric_only=True))
    print()

    # Species Similarity 
    print("Species Comparison Based on Mean Values:")
    species_means = iris.groupby("species").mean(numeric_only=True)
    print(species_means)

    print("\nInterpretation:")
    print("Species with closer average values are more similar.")
    print("Species with larger differences in averages are less similar.")

except FileNotFoundError:
    print("Error: One of the CSV files was not found.")
except Exception as e:
    print("Unexpected error:", e)
