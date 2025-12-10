import pandas as pd
import os

data = {
    'Name':["Name1","Name2", "Name3"],
    'Age':[23,24,25],
    'City':["LA", "CA", "AA"]
    }
df = pd.DataFrame(data)

new_row_v2 = {
    'Name':["Name4"],
    'Age':[26],
    'City':["KA"]
}

df.loc[len(df.index)] =new_row_v2

print(df.head())
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"CSV File saved to (file_path)")

print(df.head())