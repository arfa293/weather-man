import os
import pandas as pd

class WeatherParser:
    def __init__(self, folder_path="weatherfiles/"):  # Corrected path
        self.folder_path = folder_path

    def read_weather_data(self):
        """Reads all text weather files and returns a combined DataFrame."""
        all_data = []
        
        # Ensure the directory exists
        if not os.path.exists(self.folder_path):
            print(f"Error: Directory '{self.folder_path}' not found.")
            return pd.DataFrame()

        for file in os.listdir(self.folder_path):
            if file.endswith(".txt"):  # my files are .txt, not .csv
                file_path = os.path.join(self.folder_path, file)
                try:
                    df = pd.read_csv(file_path)  # Adjust parsing if needed
                    all_data.append(df)
                except Exception as e:
                    print(f"Error reading {file}: {e}")

        if all_data:
            return pd.concat(all_data, ignore_index=True)
        else:
            print("No valid weather files found or unable to read them.")
            return pd.DataFrame()

# **Test the Parser**
if __name__ == "__main__":
    parser = WeatherParser("weatherfiles/")  # Ensure correct path
    data = parser.read_weather_data()
    print(data.head())  # Show first few rows
