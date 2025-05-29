import pandas as pd
import os

# crearing a sample dataframe with column names
data = {'Name' : ['Alice', 'Bob', 'Charlie'],
        'Age' : [25, 30, 35],
        'City' : ['New york', 'Akkalkot', 'Mohol']
        }

df = pd.DataFrame(data)

new_row_loc = {'Name' : 'GF1', 'Age' : 20, 'City' : 'Solapur'}
df.loc[len(df.index)] = new_row_loc

# ensure the "data" directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# save the dataframe to a csv file, including column names
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")