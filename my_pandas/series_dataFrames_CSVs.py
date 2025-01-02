""" 
As I'm going with the ZTM machine learning and data science zero to mastery - series, data frames, and CSVs 
"""

import os

import pandas as pd

from helpers.utils import get_file_path, print_message  # Use absolute import

# - Pandas has 2 main data types

#! series = 1-dimensional (1 column )
series = pd.Series(["BMW", "Toyota", "Honda"])
print_message(f"Series:\n{series}")

colors = pd.Series(["Red", "Blue", "White"])
print_message(f"Colors:\n{colors}")

#! DataFrame = 2-Dimensional (multi column)
car_data = pd.DataFrame({"Car Make": series, "Color": colors})
print_message(f"DataFrame:\n {car_data}")

#! Import Data
try:
    # Search for the file in the entire project directory
    file_path = get_file_path("orders_export.csv")
    print(f"File path: {file_path}")

    # Load the CSV
    data = pd.read_csv(file_path)
    print(data)
except FileNotFoundError as e:
    print(e)
