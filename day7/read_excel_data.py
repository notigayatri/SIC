import pandas as pd
def read_excel_file():
    #Define the path to the Excel file
    file_path = r'C:\Learning\python\SIC\day7\data.csv'

    # Read the Excel file into a pandas DataFrame
    df = pd.read_csv(file_path)

	# Display the first few rows of the DataFrame
    print(df.count())
    print(df.head())
    print(df.tail())
read_excel_file()