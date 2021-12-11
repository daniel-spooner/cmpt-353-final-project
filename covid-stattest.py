# MannU-test on COVID-19 data

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import sys

covid_canada_data = "cleaned-canada-covid.csv"
covid_international_data = "cleaned-international-covid.csv"
covid_usa_data = "cleaned-usa-covid.csv"

def mannu_can_usa():
    can_covid = pd.read_csv(covid_canada_data)
    can_covid['deaths_per_100cases'] = can_covid['new_deaths'] / can_covid['new_cases'] * 100
    
    usa_covid = pd.read_csv(covid_usa_data)
    usa_covid['deaths_per_100cases'] = usa_covid['new_deaths'] / usa_covid['new_cases'] * 100
                          
    covid_mannu = stats.mannwhitneyu(can_covid['deaths_per_100cases'], usa_covid['deaths_per_100cases'])
    print(covid_mannu.pvalue)
    
    plt.figure(0)
    
    bins = np.linspace(0, 16, 24)
    plt.hist([can_covid['deaths_per_100cases'], usa_covid['deaths_per_100cases']], bins, color=['tab:blue', 'tab:orange'])
    plt.xlabel("Daily Deaths per 100 COVID-19 Cases")
    plt.legend(['Canadian Deaths per 100 Cases', 'USA Deaths per 100 Cases'])
    plt.show()
    
    
def mannu_can_int():
    can_covid = pd.read_csv(covid_canada_data)
    can_covid['deaths_per_100cases'] = can_covid['new_deaths'] / can_covid['new_cases'] * 100
    
    int_covid = pd.read_csv(covid_international_data).groupby('date').aggregate('sum')
    int_covid['deaths_per_100cases'] = int_covid['new_deaths'] / int_covid['new_cases'] * 100
                          
    covid_mannu = stats.mannwhitneyu(can_covid['deaths_per_100cases'], int_covid['deaths_per_100cases'])
    print(covid_mannu.pvalue)
    
    plt.figure(1)
    
    bins = np.linspace(0, 16, 24)
    plt.hist([can_covid['deaths_per_100cases'], int_covid['deaths_per_100cases']], bins, color=['tab:red', 'tab:green'])
    plt.xlabel("Daily Deaths per 100 COVID-19 Cases")
    plt.legend(['Canadian Deaths per 100 Cases', 'International Deaths per 100 Cases'])
    plt.show()


def mannu_can_vaccine_deaths():
    can_covid = pd.read_csv(covid_canada_data)
    can_covid['deaths_per_100cases'] = can_covid['new_deaths'] / can_covid['new_cases'] * 100
    
    median_vax = can_covid['people_vaccinated_per_hundred'].median()
    
    can_covid_lowvax = can_covid[can_covid['people_vaccinated_per_hundred'] < median_vax] 
    can_covid_highvax = can_covid[can_covid['people_vaccinated_per_hundred'] >= median_vax] 
    
    covid_mannu = stats.mannwhitneyu(can_covid_lowvax['deaths_per_100cases'], can_covid_highvax['deaths_per_100cases'])
    print(covid_mannu.pvalue)
    
    plt.figure(2)
    
    bins = np.linspace(0, 16, 24)
    plt.hist([can_covid_lowvax['deaths_per_100cases'], can_covid_highvax['deaths_per_100cases']], bins, color=['tab:blue', 'tab:orange'])
    plt.xlabel("Daily Deaths per 100 COVID-19 Cases")
    plt.legend(['Canada Low Vaccination', 'Canada High Vaccination'])
    plt.show()
    
    
def mannu_int_vaccine_deaths():
    int_covid = pd.read_csv(covid_international_data).groupby('date').aggregate('sum')
    int_covid['deaths_per_100cases'] = int_covid['new_deaths'] / int_covid['new_cases'] * 100
    
    median_vax = int_covid['people_vaccinated_per_hundred'].median()
    
    int_covid_lowvax = int_covid[int_covid['people_vaccinated_per_hundred'] < median_vax] 
    int_covid_highvax = int_covid[int_covid['people_vaccinated_per_hundred'] >= median_vax] 
    
    covid_mannu = stats.mannwhitneyu(int_covid_lowvax['deaths_per_100cases'], int_covid_highvax['deaths_per_100cases'])
    print(covid_mannu.pvalue)
    
    plt.figure(3)
    
    bins = np.linspace(0, 16, 24)
    plt.hist([int_covid_lowvax['deaths_per_100cases'], int_covid_highvax['deaths_per_100cases']], bins, color=['tab:red', 'tab:green'])
    plt.xlabel("Daily Deaths per 100 COVID-19 Cases")
    plt.legend(['International Low Vaccination', 'Internationl High Vaccination'])
    plt.show()


def mannu_can_vaccine_cases():
    can_covid = pd.read_csv(covid_canada_data)
    
    median_vax = can_covid['people_vaccinated_per_hundred'].median()
    
    can_covid_lowvax = can_covid[can_covid['people_vaccinated_per_hundred'] < median_vax] 
    can_covid_highvax = can_covid[can_covid['people_vaccinated_per_hundred'] >= median_vax] 
    
    covid_mannu = stats.mannwhitneyu(can_covid_lowvax['new_cases'], can_covid_highvax['new_cases'])
    print(covid_mannu.pvalue)
    
    plt.figure(4)
    
    #bins = np.linspace(0, 16, 24)
    plt.hist([can_covid_lowvax['new_cases'], can_covid_highvax['new_cases']], bins=12, color=['tab:blue', 'tab:orange'])
    plt.xlabel("Daily COVID-19 Cases")
    plt.legend(['Canada Low Vaccination', 'Canada High Vaccination'])
    plt.show()
    

def main():
    mannu_can_usa()
    mannu_can_int()
    mannu_can_vaccine_deaths()
    mannu_int_vaccine_deaths()
    mannu_can_vaccine_cases()


if __name__ == '__main__':
        main()
