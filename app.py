import pandas as pd
import os

file_path = "/mount/src/hello/movies.csv"

try:
    data = pd.read_csv(file_path)
    print("File read successfully.")
except Exception as e:
    print(f"Error reading the file: {e}")
