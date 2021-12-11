# COVID-19 Data Analysis

## Installation
---
### Python
```
sudo apt-get install python3.8
```
### Install Required Packages
```
python -m pip install -U pip wheel
python -m pip install -U numpy pandas matplotlib scipy statsmodels scikit-image keras jupyter notebook
```
## Download Data

Download complete COVID-19 dataset from  
`https://github.com/owid/covid-19-data/tree/master/public/data`

https://covid.ourworldindata.org/data/owid-covid-data.csv


## Run Instructions
---
Run data_processing.py to get datafiles for `anova.ipynb`, `covid-stattest.py`, and `covid.ipynb`.

```
python data_processing.py [path_to_owid_csv]
```
Place created data files in `clean_data/`

### `avova.ipynb`
Open notebook, and run all cells.

### `covid-stattest.py`
```
python covid-stattest.py
```

### `covid.ipynb`
Open notebook, and run all cells.
