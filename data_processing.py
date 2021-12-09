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
    select_data.to_csv(out_name, index=False)
    
    
def cleanCanadaVaccine(path):
    print("Cleaning Canada Vaccine Data...")
    full_path = path + filenames[1]
    data = pd.read_csv(full_path)
    
    select_data = data[['week_end', 'prename', 'numtotal_atleast1dose', 'numtotal_partially', 'numtotal_fully',
                        'numeligible_atleast1dose', 'numeligible_partially', 'numeligible_fully']]
    
    out_name = 'cleaned-' + filenames[1]
    select_data.to_csv(out_name, index=False)


def cleanInternationalCovid(path):
    print("Cleaning International Covid Data...")
    full_path = path + filenames[2]
    data = pd.read_csv(full_path)
    
    select_data = data[['iso_code', 'date', 'new_cases', 'new_cases_14_days', 'new_cases_14_days_100k', 'total_cases',
                        'total_cases_100k', 'new_deaths_14_days', 'new_deaths_14_days_100k', 'total_deaths',
                        'total_deaths_100k']]
    
    out_name = 'cleaned-' + filenames[2]
    select_data.to_csv(out_name, index=False)


def cleanUSACovid(path):
    print("Cleaning USA Covid Data...")
    full_path = path + filenames[3]
    data = pd.read_csv(full_path, parse_dates=['submission_date'])
    
    select_data = data[['submission_date', 'state', 'tot_cases', 'conf_cases', 'prob_cases', 'new_case', 'tot_death',
                        'new_death']]
    select_data = select_data.dropna()
    select_data = select_data.sort_values('submission_date')
    
    out_name = 'cleaned-' + filenames[3]
    select_data.to_csv(out_name, index=False)
    
    
def cleanUSAVaccine(path):
    print("Cleaning USA Vaccine Data...")
    full_path = path + filenames[4]
    data = pd.read_csv(full_path, dtype={'FIPS': "string"})
    
    select_data = data[['Date', 'Recip_State', 'Administered_Dose1_Recip', 'Administered_Dose1_Pop_Pct']]
    select_data = select_data.groupby(['Recip_State', 'Date'], as_index=False).aggregate('mean')
    select_data = select_data.rename(columns={'Date': 'date', 'Recip_State': 'state', 'Administered_Dose1_Recip': 'dose1',
                                              'Administered_Dose1_Pop_Pct': 'dose1_pct'})
    
    out_name = 'cleaned-' + filenames[4]
    select_data.to_csv(out_name, index=False)


def main(path):
    cleanCanadaCovid(path)
    cleanCanadaVaccine(path)
    cleanInternationalCovid(path)
    cleanUSACovid(path)
    cleanUSAVaccine(path)


if __name__ == '__main__':
    if(len(sys.argv) > 1):
        data_directory = sys.argv[1] + '/'
        main(data_directory)
    else:
        main('')

