import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Hackathon\DGCA_DATA.csv')

# Convert 'Month' to datetime format
df['Month'] = pd.to_datetime(df['Month'], format='%m/%Y')
df = df.sort_values('Month')
df = df.dropna()

# Function to plot ASK vs Passenger Demand
def plot_ask_vs_passenger_demand(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Month'], df['Avail Seats Km(millions)'], label='ASK (millions)', marker='o', linestyle='-')
    plt.plot(df['Month'], df['Km Performed(Millions)(P)'], label='Passenger Demand (millions)', marker='s', linestyle='--')
    plt.xlabel("Month")
    plt.ylabel("Millions of Kilometers")
    plt.title("Available Seat Kilometers (ASK) vs Passenger Demand Over Time")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Function to analyze flight hours vs passengers carried
def plot_flight_hours_vs_passengers(df):
    correlation = df[['Hours (AF)', 'No Carried(P)']].corr()
    print("Correlation Matrix (Flight Hours vs. Passengers):\n", correlation)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df['Hours (AF)'], y=df['No Carried(P)'])
    plt.xlabel("Flight Hours")
    plt.ylabel("Passengers Carried")
    plt.title("Correlation Between Flight Hours and Passengers Carried")
    plt.grid(True)
    plt.show()

# Function to analyze freight trends over time
def plot_freight_trends(df):
    df['Year'] = df['Month'].dt.year
    df['Month_Num'] = df['Month'].dt.month
    pivot_freight = df.pivot_table(values='Freight TON KM Performed', index='Year', columns='Month_Num', aggfunc='sum')
    plt.figure(figsize=(12, 6))
    sns.heatmap(pivot_freight, cmap="coolwarm", annot=True, fmt=".0f")
    plt.title("Freight Transport Trends (Heatmap)")
    plt.xlabel("Month")
    plt.ylabel("Year")
    plt.show()

def load_data():
    df = pd.read_csv('Hackathon/DGCA_DATA.csv')
    df['Month'] = pd.to_datetime(df['Month'], format='%m/%Y')
    df = df.sort_values('Month').dropna()
    return df

def display_menu():
    print("\nAviation Data Analysis Menu:")
    print("1. Plot ASK vs Passenger Demand")
    print("2. Analyze Flight Hours vs Passengers Carried")
    print("3. Analyze Freight Trends Over Time")
    print("0. Exit")

def main():
    df = load_data()
    while True:
        display_menu()
        choice = input("Enter your choice (0 for exit): ")
        
        match choice:
            case '1':
                plot_ask_vs_passenger_demand(df)
            case '2':
                plot_flight_hours_vs_passengers(df)
            case '3':
                plot_freight_trends(df)
            case '0':
                print("Exiting program.")
                break
            case _:
                print("Invalid choice. Please select a number between 0 and 15.")

if __name__ == "__main__":
    main()