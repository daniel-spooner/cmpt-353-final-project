# Cleaning COVID-19 data files

import pandas as pd
import sys

filenames = ['canada-covid.csv', 'canada-vaccination.csv',
             'international-covid.csv', 'usa-covid.csv', 'usa-vaccination.csv']
outdir = 'cleaned_data/'

def cleanCanadaCovid(path):
    print("Cleaning Canada Covid Data...")
    full_path = path + filenames[0]
    data = pd.read_csv(full_path)
    
    select_data = data[['prname', 'date', 'numconf', 'numprob', 'numdeaths', 'numtotal', 'numtoday', 'numdeathstoday',
                        'numactive', 'numtotal_last14', 'numdeaths_last14', 'numtotal_last7', 'numdeaths_last7']]
    
    out_name = 'cleaned-' + filenames[0]
    select_data.to_csv(out_name)
    
def cleanCanadaVaccine(path):
    print("Cleaning Canada Vaccine Data...")
    full_path = path + filenames[1]
    data = pd.read_csv(full_path)
    
    select_data = data[['week_end', 'prename', 'numtotal_atleast1dose', 'numtotal_partially', 'numtotal_fully',
                        'numeligible_atleast1dose', 'numeligible_partially', 'numeligible_fully']]
    
    out_name = 'cleaned-' + filenames[1]
    select_data.to_csv(out_name)

def cleanInternationalCovid(path):
    print("Cleaning International Covid Data...")
    full_path = path + filenames[2]
    data = pd.read_csv(full_path)
    
    select_data = data[['iso_code', 'date', 'new_cases', 'new_cases_14_days', 'new_cases_14_days_100k', 'total_cases',
                        'total_cases_100k', 'new_deaths_14_days', 'new_deaths_14_days_100k', 'total_deaths',
                        'total_deaths_100k']]
    
    out_name = 'cleaned-' + filenames[2]
    select_data.to_csv(out_name)

def cleanUSACovid(path):
    print("Cleaning USA Covid Data...")
    full_path = path + filenames[3]
    data = pd.read_csv(full_path)
    pass
    
def cleanUSAVaccine(path):
    print("Cleaning USA Vaccine Data...")
    full_path = path + filenames[4]
    data = pd.read_csv(full_path)
    pass


def main(path):
    cleanCanadaCovid(path)
    cleanCanadaVaccine(path)
    cleanInternationalCovid(path)
    #cleanUSACovid(path)
    #cleanUSAVaccine(path)


if __name__ == '__main__':
    if(len(sys.argv) > 1):
        data_directory = sys.argv[1] + '/'
        main(data_directory)
    else:
        main('')

