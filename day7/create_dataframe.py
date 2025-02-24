import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)
print(df)
grouped = df.groupby('Age')['Salary'].mean() 
# Groups by Age and calculates mean salary
print(grouped)