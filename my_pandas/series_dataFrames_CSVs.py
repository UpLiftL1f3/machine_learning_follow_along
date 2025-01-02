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
    order_processing_data = pd.read_csv(file_path)
    print_message(order_processing_data)
except FileNotFoundError as e:
    print(e)

#! Exporting a DataFrame
# Get the directory of the current script
current_script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the file path for the CSV file
output_file_path = os.path.join(current_script_dir, "exported_car_sales.csv")
# Export the DataFrame to the file path
# -> The below code is commented out to prevent recreating the file every time I run the file
# TODO: car_data.to_csv(output_file_path, index=False)
# * Read the CSV File
car_sales_file_path = get_file_path("exported_car_sales.csv")
car_sales_data = pd.read_csv(car_sales_file_path)
print_message(car_sales_data)


#! Describe Data
print_message(order_processing_data.dtypes)
