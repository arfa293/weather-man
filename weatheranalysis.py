import os
import pandas as pd

def load_weather_data(directory):
    all_data = []

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            df = pd.read_csv(file_path, delimiter=",", skipinitialspace=True)

            df.columns = df.columns.str.strip()  # Remove spaces

            if 'PKT' not in df.columns:
                print(f"ERROR: 'PKT' column not found in {filename}")
                continue
            
            df['PKT'] = pd.to_datetime(df['PKT'], errors='coerce')  # Convert PKT to datetime
            df['Year'] = df['PKT'].dt.year
            df['Month'] = df['PKT'].dt.month

            all_data.append(df)

    if not all_data:
        print("ERROR: No valid data found in directory")
        return pd.DataFrame()

    return pd.concat(all_data, ignore_index=True)


def yearly_extremes(df):
    if df.empty:
        print("No data available for analysis.")
        return
    
    result = df.groupby('Year').agg({
        'Max TemperatureC': 'max',
        'Min TemperatureC': 'min',
        'Max Humidity': 'max'
    }).reset_index()

    print("\nYearly Extreme Temperatures & Humidity:")
    print(result)
    return result
def monthly_averages(df):
    if df.empty:
        print("No data available for analysis.")
        return
    
    result = df.groupby(['Year', 'Month']).agg({
        'Mean TemperatureC': 'mean',
        'Mean Humidity': 'mean'
    }).reset_index()

    print("\nMonthly Average Temperatures & Humidity:")
    print(result)
    return result
import matplotlib.pyplot as plt

def plot_monthly_temperatures(df, year):
    df_year = df[df['Year'] == year]
    
    if df_year.empty:
        print(f"No data found for the year {year}")
        return

    monthly_avg = df_year.groupby('Month')['Mean TemperatureC'].mean()

    plt.figure(figsize=(10, 5))
    plt.bar(monthly_avg.index, monthly_avg.values, color='skyblue')
    plt.xlabel("Month")
    plt.ylabel("Average Temperature (°C)")
    plt.title(f"Average Monthly Temperatures in {year}")
    plt.xticks(range(1, 13))
    plt.show()

directory = "weatherfiles"  # Change to your actual directory
df = load_weather_data(directory)

yearly_extremes(df)
monthly_averages(df)
plot_monthly_temperatures(df, 2024)  # Change 2024 to any year you want to visualize
