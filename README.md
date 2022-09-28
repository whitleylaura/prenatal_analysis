# Analysis of CDC Birth Records 2016-2021 (in progress)

Data Source: https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm (under section "Birth Data Files")
* Files unzip to .txt files where each line of 1330 characters represents 1 birth record
* User Guide (under section "Birth Data Files) provides information on what variables each character space represents

## Process
1. Due to size of each file and limitations of my PC I first selected around 20 variables of interest and parsed the .txt file to a .csv of the smaller desired data using subset_data.py
** test script (see folder) validated that parsing correctly selected variables from raw .txt
3. Parsing had to be done in small chunks (again due to limitations of RAM and storage in PC), so once a year was parsed fully the smaller .csv files were rejoined using merge.py 
4. Full years of subsetted data were then sorted by columns representing important sociodemographic factors using sort_by.py
* race_hispanic_orign
* pay_recode (payment type: Medicaid, Private, Self-Pay, Other)
* mothers_age
* education_mom
5. Summary statistics on the column prenatal_num (depicting # of prenatal visits throughout pregnancy) for each variable under a sociodemographic factor were then calculated and written to a .csv by pnum_calcs.py

Most scripts employed command line arguments so one script could be used to process several different inputs & variables

## Upcoming

Summary statistics for prenatal_num  are represented in .csv within stats folder. I plan to graph and run statistical analyses on them in R, but a quick look at the data does seem to reveal a pattern matching known variations of sociodemographic factors (those factors typically associated with worse maternal outcomes also tend to have lower average number of prenatal visits)
