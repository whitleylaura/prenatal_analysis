"""
filename: sort_by.py

program creation date: August 23rd, 2022

Takes csv files of all birth records for a particular year and sorts them
into individual csv files based on a particular column
(ex: sort_by.py -i full_output.csv -c pay_recode -p pay_recode creates
a csv for each payment type - Medicaid, Private, Self-Pay, Other, &
Unknown that allows for more in depth analysis to be done on each)
"""
# import packages
import argparse
import pandas as pd
import time
import sys


def main():
    """
    business logic
    :return: csv for each
    """
    start = time.time()
    args = get_cli_args()
    infile = str(args.INFILE)
    column_name = str(args.COLUMN).lower()
    path = str(args.PATH)
    data = csv_to_dataframe(infile)
    # check that column name does exist
    if check_column_name(data, column_name) is False:
        print(f'\nColumn name does not exist in infile\n')
        sys.exit(1)
    else:
        sort_by(data, column_name, path)
    end = time.time()
    total_time = end - start
    print("\n" + str(total_time))


def csv_to_dataframe(infile):
    """
    :param infile: file handle for incoming file
    :return: dataframe of information from infile
    """
    df = pd.read_csv(infile)
    return df


def check_column_name(df, column_name):
    """
    :param df: dataframe of infile from csv_to_dataframe(infile) function
    :param column_name: user input column name
    :return: Boolean based on whether column is present in data
    """
    names = list(df)
    if column_name in names:
        return True
    else:
        return False


def sort_by(data, name, path):
    """
    :param data: dataframe of infile from csv_to_dataframe(infile) function
    :param name: user input column name
    :param path: path to folder for containing output
    :return: individual csv files for each unique variable in a column
    """
    # create list of unique column values
    unique = data[str(name)].unique()
    print(unique)
    # create a data frame dictionary to store your data frames
    DataFrameDict = {elem: pd.DataFrame() for elem in unique}

    for key in DataFrameDict.keys():
        DataFrameDict[key] = data[:][data[str(name)] == key]

    for key in DataFrameDict.keys():
        df = DataFrameDict[key]
        name = "{}.csv".format(key)
        df.to_csv(str(path+"/"+name))
        print(key)


def get_cli_args():
    """
    function specifies command line inputs
    :return: information needed for program to continue
    """
    parser = argparse.ArgumentParser(description='Provide input and output filenames for program')

    parser.add_argument('-i', '--infile',
                        dest='INFILE',
                        type=str,
                        help='Path to the file to open',
                        required=False,
                        default="sample.csv")
    parser.add_argument('-c', '--column',
                        dest='COLUMN',
                        type=str,
                        help='Column name to sort by',
                        required=True)
    parser.add_argument('-p', '--path',
                        dest='PATH',
                        type=str,
                        help='Path to folder for output',
                        required=True)

    return parser.parse_args()


if __name__ == '__main__':
    main()
