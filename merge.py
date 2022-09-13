"""
filename: merge.py

program creation date: August 27th, 2022

Due to the processing limitations of my personal computer I had to divide
the birth record files into multiple parts to run the subset_data.py script.
All the output csv files from the program were saved in a directory (named
subset) so the following script iterates through the different files present
in the directory and merges them into a single csv for subsequent analysis.
"""
# import packages
import pandas as pd
import glob
import os

root_dir = "/Users/laurawhitley/PycharmProjects/prenatal_analysis/subset/"
files = os.path.join(root_dir, "output*.csv")
files = glob.glob(files)
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
df.to_csv(str(root_dir + "full_output.csv"))