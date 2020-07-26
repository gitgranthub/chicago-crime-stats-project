# CHICAGO CRIME & WELL-BEING  
## Group Project (State Level Analysis)

Data Science and Visualization Boot Camp (Northwestern University)

![GitHub last commit](https://img.shields.io/github/last-commit/OlegRyzhkov2020/api-challenge)
![GitHub top language](https://img.shields.io/github/languages/top/OlegRyzhkov2020/api-challenge)
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)
[![HitCount](http://hits.dwyl.com/OlegRyzhkov2020/api-challenge.svg)](http://hits.dwyl.com/OlegRyzhkov2020/api-challenge)
![GitHub watchers](https://img.shields.io/github/watchers/OlegRyzhkov2020/api-challenge?label=Watch&style=social)
![GitHub followers](https://img.shields.io/github/followers/OlegRyzhkov2020?label=Follow&style=social)

![presentation_slide](images/slide_question.png)

## Data sources

![presentation_slide](images/slide_data.png)

## Data cleaning and updating

```python
 def cities_coord(df):
    for row in df.itertuples():
        client = GoogleMapClient(api_key = g_key, address_or_postal_code = f'{row.City}')
        try:
            df.loc[row.Index, 'Lat'] = client.lat
            df.loc[row.Index, 'Lng'] = client.lng
        except:
            pass
        if row.Index % 30 == 0:
            print('Processing records: found ', row.Index,' cities')
    print('\nProcessing is over\n')
    return df
```

## Data exploration

![exploration](images/normality.png)

![exploration](images/exploration_2011.png)

## Data Visualization

![final_map](images/death_rate_2011.png)

![final_map](images/crime_rate_2011.png)

## Statistical Analysis

```python
# Regression Analysiss for 2011
crime_pov = DataAnalysis(expl_data_2011['Crime Rate'], expl_data_2011['Poverty Rate'])
crime_lat = DataAnalysis(expl_data_2011['Crime Rate'], expl_data_2011['Latitude'])

# using the variable axs for multiple Axes
plt.figure(figsize=(25, 4))
plt.subplot(131)
plt.suptitle('Simple Linear Regression Analysis for Crime Rate, 2011', x= 0.35, y=1.05, size=16)
crime_pov.scat_plot()
plt.subplot(132)
crime_lat.scat_plot()
```

![analysis](images/simple_regression.png)

## Contacts
[Find Me on
LinkedIn](https://www.linkedin.com/in/oleg-n-ryzhkov/)
