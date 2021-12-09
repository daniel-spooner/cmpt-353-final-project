# Cleaning COVID-19 data files

import pandas as pd
import sys

filename = 'owid-covid-data.csv'


def cleanCanadaCovid(path):
    print("Cleaning Canada Covid Data...")
    full_path = path + filename
    data = pd.read_csv(full_path, parse_dates=['date'])
    data = data[data['iso_code'] == 'CAN']

    select_data = data[['iso_code', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 
                        'total_cases_per_million', 'new_cases_per_million', 'total_deaths_per_million',
                        'new_deaths_per_million', 'people_vaccinated', 'people_vaccinated_per_hundred']]
    
    out_name = 'cleaned-canada-covid.csv'
    select_data.to_csv(out_name, index=False)

def cleanInternationalCovid(path):
    print("Cleaning International Covid Data...")
    full_path = path + filename
    data = pd.read_csv(full_path, parse_dates=['date'])

    select_data = data[['iso_code', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 
                        'total_cases_per_million', 'new_cases_per_million', 'total_deaths_per_million',
                        'new_deaths_per_million', 'people_vaccinated', 'people_vaccinated_per_hundred']]
    
    out_name = 'cleaned-international-covid.csv'
    select_data.to_csv(out_name, index=False)


def cleanUSACovid(path):
    print("Cleaning USA Covid Data...")
    full_path = path + filename
    data = pd.read_csv(full_path, parse_dates=['date'])
    data = data[data['iso_code'] == 'USA']

    select_data = data[['iso_code', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 
                        'total_cases_per_million', 'new_cases_per_million', 'total_deaths_per_million',
                        'new_deaths_per_million', 'people_vaccinated', 'people_vaccinated_per_hundred']]
    
    out_name = 'cleaned-usa-covid.csv'
    select_data.to_csv(out_name, index=False)
    print(select_data.dtypes)


def main(path):
    cleanCanadaCovid(path)
    cleanInternationalCovid(path)
    cleanUSACovid(path)
    print("Success")


if __name__ == '__main__':
    if(len(sys.argv) > 1):
        data_directory = sys.argv[1] + '/'
        main(data_directory)
    else:
        main('')
