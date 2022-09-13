"""
filename: subset_data.py

program creation date: August 10th, 2022

This program iterates through birth records to select desired data
"""
# import packages
import argparse
import pandas as pd
import time


def main():
    """
    business logic
    :return: selected columns in output csv
    """
    start = time.time()
    args = get_cli_args()
    infile = str(args.INFILE)
    outfile = str(args.OUTFILE)
    select_columns(infile, outfile)
    end = time.time()
    total_time = end - start
    print("\n" + str(total_time))


def select_columns(infile, outfile):
    """
    parses birth record lines for desired information
    :return: csv file with dataframe
    """
    cols = ['birth_place', 'simple_birthplace', 'mothers_age', 'race_hispanic_origin', 'education_mom',
            'prenatal_began_month', 'simple_prenatal_began', 'prenatal_num', 'prenatal_recode',
            'previous_cesarean', 'cesarean_num', 'risk_reported', 'ld_induction', 'ld_aug', 'ld_steroids',
            'ld_antibiotics', 'ld_chorio', 'ld_anesthesia', 'delivery_method', 'trial_labor', 'delivery_recode',
            'delivery_recode2', 'birth_attendant', 'pay', 'pay_recode', 'breastfed_discharge']
    df = pd.DataFrame(columns=cols)

    with open(infile, "r") as file:
        for count, line in enumerate(file):
            # numbers adjusted from data guide to account for 0 based counting system in python
            birth_place = line[31:32]
            simple_birthplace = line[49:50]
            mothers_age = line[76:78]
            race_origin = line[116:117]
            edu = line[123:124]
            prenatal = line[223:225]
            prenatal2 = line[226:227]
            pre3 = line[237:239]
            pre_re = line[241:243]
            pre_c = line[330:331]
            num_c = line[331:333]
            risk = line[336:337]
            ld1 = line[382:383]
            ld2 = line[383:384]
            ld3 = line[384:385]
            ld4 = line[385:386]
            ld5 = line[386:387]
            ld6 = line[387:388]
            deliv = line[401:402]
            trial = line[402:403]
            deliv_re = line[406:407]
            deliv_re2 = line[407:408]
            birth_a = line[432:433]
            pay = line[434:435]
            pay_re = line[435:436]
            breastfed = line[568:569]
            df.loc[len(df.index)] = [birth_place, simple_birthplace, mothers_age, race_origin, edu, prenatal, prenatal2,
                                     pre3, pre_re, pre_c, num_c, risk, ld1, ld2, ld3, ld4, ld5, ld6, deliv, trial,
                                     deliv_re, deliv_re2, birth_a, pay, pay_re, breastfed]
            print(count)

    df.to_csv(outfile, encoding='utf-8')


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
                        required=True)
    parser.add_argument('-o', '--outfile',
                        dest='OUTFILE',
                        type=str,
                        help='Path to the file to write output',
                        required=True)

    return parser.parse_args()


if __name__ == '__main__':
    main()
