
import pandas as pd
import os

# Get project folder location
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath())
)

# Dataset path
DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "merged_air_quality.xls"
)

# Check dataset exists
if not os.path.exists(DATA_PATH):
    print("Dataset file not found!")
else:
    # Load Excel dataset
    df = pd.read_excel(DATA_PATH)

    # Display first 5 records
    print("\nFIRST 5 RECORDS")
    print(df.head())

    # Display dataset shape
    print("\nDATASET SHAPE")
    print(df.shape)

    # Display column names
    print("\nCOLUMN NAMES")
    print(df.columns.tolist())

    # Display dataset information
    print("\nDATASET INFORMATION")
    df.info()

    # Check missing values
    print("\nMISSING VALUES")
    print(df.isnull().sum())

    # Check duplicate records
    print("\nDUPLICATE RECORDS")
    print(df.duplicated().sum())

