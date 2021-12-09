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

    select_data = data[['prname', 'date', 'numtotal', 'numtoday', 'numdeaths', 'numdeathstoday']]
    select_data = select_data.rename(columns={'prname': 'province', 'date': 'date', 'numtotal': 'cases_total', 
                                              'numtoday': 'cases_daily', 'numdeaths': 'deaths_total',
                                              'numdeathstoday': 'deaths_daily'})
    
    out_name = 'cleaned-' + filenames[0]
    select_data.to_csv(out_name)
    
    
def cleanCanadaVaccine(path):
    print("Cleaning Canada Vaccine Data...")
    full_path = path + filenames[1]
    data = pd.read_csv(full_path)
    
    select_data = data[['week_end', 'prename', 'numtotal_atleast1dose', 'proptotal_atleast1dose']]
    select_data = select_data.rename(columns={'week_end': 'date', 'prename': 'province', 'numtotal_atleast1dose': 'dose1', 
                                              'proptotal_atleast1dose': 'dose1_pct'})
    
    out_name = 'cleaned-' + filenames[1]
    select_data.to_csv(out_name)


def cleanInternationalCovid(path):
    print("Cleaning International Covid Data...")
    full_path = path + filenames[2]
    data = pd.read_csv(full_path)
    
    select_data = data[['iso_code', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]
    select_data = select_data.rename(columns={'iso_code': 'country', 'date': 'date', 'total_cases': 'cases_total', 
                                          'new_cases': 'cases_daily', 'total_deaths': 'deaths_total',
                                          'new_deaths': 'deaths_daily'})

    out_name = 'cleaned-' + filenames[2]
    select_data.to_csv(out_name)


def cleanUSACovid(path):
    print("Cleaning USA Covid Data...")
    full_path = path + filenames[3]
    data = pd.read_csv(full_path, parse_dates=['submission_date'])
    
    select_data = data[['submission_date', 'state', 'tot_cases', 'new_case', 'tot_death', 'new_death']]
    select_data = select_data.rename(columns={'state': 'state', 'submission_date': 'date', 'tot_cases': 'cases_total', 
                                              'new_case': 'cases_daily', 'tot_death': 'deaths_total',
                                              'new_death': 'deaths_daily'})
    select_data = select_data.dropna()
    select_data = select_data.sort_values('date')
    
    
    out_name = 'cleaned-' + filenames[3]
    select_data.to_csv(out_name)
    
    
def cleanUSAVaccine(path):
    print("Cleaning USA Vaccine Data...")
    full_path = path + filenames[4]
    data = pd.read_csv(full_path, dtype={'FIPS': "string"})
    
    select_data = data[['Date', 'Recip_State', 'Administered_Dose1_Recip', 'Administered_Dose1_Pop_Pct']]
    select_data = select_data.groupby(['Recip_State', 'Date'], as_index=False).aggregate('mean')
    select_data = select_data.rename(columns={'Date': 'date', 'Recip_State': 'state', 'Administered_Dose1_Recip': 'dose1',
                                              'Administered_Dose1_Pop_Pct': 'dose1_pct'})
    
    out_name = 'cleaned-' + filenames[4]
    select_data.to_csv(out_name)


def main(path):
    cleanCanadaCovid(path)
    cleanCanadaVaccine(path)
    cleanInternationalCovid(path)
    cleanUSACovid(path)
    cleanUSAVaccine(path)
    print("Success")


if __name__ == '__main__':
    if(len(sys.argv) > 1):
        data_directory = sys.argv[1] + '/'
        main(data_directory)
    else:
        main('')
