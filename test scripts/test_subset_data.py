"""Test suite for create_dataframe.py"""
import subset_data


FILE_2_TEST = "sample.txt"
OUTFILE_TEST = "sample.csv"
correct_csv = "correct_output.csv"


def text_compare(fl1, fl2):
    file1 = open(fl1, 'r')
    file2 = open(fl2, 'r')
    lines1 = file1.readlines()
    lines2 = file2.readlines()
    file1.close()
    file2.close()
    if lines1 == lines2:
        return True
    else:
        print(lines1)
        print(lines2)


def test_select_columns():
    subset_data.select_columns(FILE_2_TEST, OUTFILE_TEST)
    assert text_compare(correct_csv, OUTFILE_TEST) is True, "files do not match"

