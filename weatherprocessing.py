import pandas as pd
import os

def load_weather_data(directory):
    all_data = []

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            df = pd.read_csv(file_path, delimiter=",", skipinitialspace=True)  # Remove spaces

            print(f"Reading file: {filename}")
            print("First few rows of the file:")
            print(df.head())  # Debugging
            print(f"Columns found: {df.columns.tolist()}")  # Check column names

            # Strip spaces from column names
            df.columns = df.columns.str.strip()

            # Check if 'PKT' column exists
            if 'PKT' not in df.columns:
                print(f"ERROR: 'PKT' column not found in {filename}")
                continue  # Skip this file
            
            # Convert PKT to datetime format
            df['PKT'] = pd.to_datetime(df['PKT'], errors='coerce')

            all_data.append(df)

    if not all_data:
        print("ERROR: No valid data found in directory")
        return pd.DataFrame()  # Return empty DataFrame if no valid data

    return pd.concat(all_data, ignore_index=True)
