"""
filename: pnum_calcs.py

program creation date: August 27th, 2022

Takes in folders of variable types (each csv represents one variable for the type)
and outputs summary statistics for each variable in CSVs
"""
# import packages
import argparse
import pandas as pd
import time
import os
import glob


def main():
    """
    business logic
    :return: csv with summary statistics
    """
    start = time.time()
    args = get_cli_args()
    path = str(args.PATH)
    root = "/Users/laurawhitley/PycharmProjects/MaternalOutcomes/"
    final_path = str(root + path)
    files = os.path.join(final_path, "*.csv")
    files = glob.glob(files)
    print(files)
    # num of files in folder varies, os & glob allow this script to work for all
    for item in files:
        df = pd.read_csv(item)
        data = df[df.prenatal_num != 99]
        match = os.path.basename(item)
        data["prenatal_num"].describe().to_csv(str(final_path + "/pn_calc" + match))
        # performs calculations and writes summary stats to csv
        print(match)
    end = time.time()
    total_time = end - start
    print("\n" + str(total_time))


def get_cli_args():
    """
    function specifies command line inputs
    :return: information needed for program to continue
    """
    parser = argparse.ArgumentParser(description='Provide input file path for program')

    parser.add_argument('-p', '--path',
                        dest='PATH',
                        type=str,
                        help='Path to the folder for analysis',
                        required=True)

    return parser.parse_args()


if __name__ == '__main__':
    main()
