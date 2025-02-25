import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_ask_vs_passenger_demand(df):
    """Plot Available Seat Kilometers (ASK) vs Passenger Demand over time."""
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

def plot_flight_hours_vs_passengers(df):
    """Plot the relationship between flight hours and passengers carried."""
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df['Hours (AF)'], y=df['No Carried(P)'])
    plt.xlabel("Flight Hours")
    plt.ylabel("Passengers Carried")
    plt.title("Correlation Between Flight Hours and Passengers Carried")
    plt.grid(True)
    plt.show()

def plot_freight_mail_fluctuation(df):
    """Plot heatmap to visualize freight transport fluctuations over time."""
    df['Year'] = df['Month'].dt.year
    df['Month_Num'] = df['Month'].dt.month
    
    pivot_freight = df.pivot_table(values='Freight TON KM Performed', index='Year', columns='Month_Num', aggfunc='sum')
    plt.figure(figsize=(12, 6))
    sns.heatmap(pivot_freight, cmap="coolwarm", annot=True, fmt=".0f")
    plt.title("Freight Transport Trends (Heatmap)")
    plt.xlabel("Month")
    plt.ylabel("Year")
    plt.show()

# Main execution
file_path = 'Hackathon/DGCA_DATA.csv'
df = pd.read_csv(file_path)
df['Month'] = pd.to_datetime(df['Month'], format='%m/%Y')
df = df.sort_values('Month').dropna()

plot_ask_vs_passenger_demand(df)
plot_flight_hours_vs_passengers(df)
plot_freight_mail_fluctuation(df)
