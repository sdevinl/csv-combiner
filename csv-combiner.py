#!/usr/bin/env python3
import sys
import pandas as pd

args = sys.argv
dfs = []

# csv to dataframes
for i in range(1, len(args)):

    # read file path to df
    df = pd.read_csv(args[i])
    # get filename
    fn = args[i].split('/')[2]
    # create filename column
    df['filename'] = fn
    # append dfs to array
    dfs.append(df)

# concatenate all dfs
final_df = pd.concat(dfs)

# convert to csv
final_csv = final_df.to_csv('')

if __name__ == "__main__":
    print(final_csv)
    
'''if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")'''
