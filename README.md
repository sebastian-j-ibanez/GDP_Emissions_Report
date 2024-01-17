
# Emissions vs GDP

This report outlines the research performed by several students at Conestoga College to examine GDP, emissions, and their relationship. The report compared linear, exponential, and polynomial regression to determine which model most accurately demonstrated the relationship between GDP and CO2 emissions. The full PDF is found in the *report* folder.

## Models

The research outlined various countries GDP, emissions, and their correlation. Figures 2-4 were generate using emissions_gdp.py. Figure 5 was generate using correlation.py. Figures 6-10 were generated using the various linear, exponential and polynomial files found in the *model* folder.

## Datasets

GDP data has been sourced from the 2021 World Bank report and the 2022 The Global Carbon Project's 2022 emissions dataset. The datasets are stored in the *data* folder.

## Requirements

This project has been built using python 3.10. Older versions of Python are not guaranteed to work. Project dependencies are found in requirements.txt.

## Setup

This project can be setup by with the following commands:

```bash
git clone ...
cd Report
pip install -r requirements.txt
```
To run a model, enter the *models* folder and run the desired file. For example I wanted to use *correlation.py*:

```bash
cd models
py correlation.py
```
