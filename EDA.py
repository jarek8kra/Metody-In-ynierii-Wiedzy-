# Działania na danych
import pandas as pd
import numpy as np
import scipy.stats as st
import missingno as msno

# Wizualizacja
import matplotlib.pyplot as plt
import seaborn as sns

# Setup
#matplotlib inline
sns.set()
# Załadujemy dane odnośnie Covid-19
# Link do źródła: https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset/data
covid_data = pd.read_csv(
    'covid_19_data.csv',
    index_col='SNo',
    parse_dates=['ObservationDate', 'Last Update']
)

# Zacznijmy od sprawdzenia rozmiaru naszego datasetu.
print(f'Ilość wierszy: {covid_data.shape[0]}')
print(f'Ilość kolumn: {covid_data.shape[1]}')


# Informacje o naszym zbiorze danych
covid_data.info()

# Opiszemy dane by zobaczyć podstawowe statystyki wartości numerycznych
covid_data.describe()

# Początek zbioru danych
covid_data.head()

# Koniec zbioru danych
covid_data.tail()


# Wartości kategoryczne
covid_data_categorical = covid_data.select_dtypes(include=[np.object])
covid_data_categorical.columns

# Wartości numeryczne
covid_data_numeric = covid_data.select_dtypes(include=[np.number])
covid_data_numeric.columns

# Wyświetl jako matrix
msno.matrix(covid_data)

# Wyświetl jako bar plot
msno.bar(covid_data)

# Zobaczmy te puste wartości
covid_data[covid_data['Province/State'].isna()].head(20)

# Kurtoza
covid_data.kurt()

# Skośność
covid_data.skew()

# Wykres kurtozy
sns.distplot(covid_data.kurt())

# Wykres skośności
sns.distplot(covid_data.skew())

# Korelacje między wartościami numerycznymi
sns.heatmap(covid_data.corr())

# Pair plot pokazujący jak zachowują się wartości względem siebie
sns.pairplot(data=covid_data, markers='x')

# Dane dla Polski
poland_data = covid_data[covid_data['Country/Region'] == 'Poland']
poland_data.head(10)

# Wizualizacja danych czasowych
figure, ax = plt.subplots(2,1)
sns.lineplot(
    x='ObservationDate',
    y='Confirmed',
    data=poland_data,
    label='Potwierdzone',
    color='blue',
    ax=ax[0],
)
sns.lineplot(
    x='ObservationDate',
    y='Deaths',
    data=poland_data,
    label='Zgony',
    color='black',
    ax=ax[0],
)
sns.lineplot(
    x='ObservationDate',
    y='Recovered',
    data=poland_data,
    label='Wyzdrowienia',
    color='green',
    ax=ax[0]
)

# Bez confirmed, by było lepiej widać
sns.lineplot(
    x='ObservationDate',
    y='Deaths',
    data=poland_data,
    label='Zgony',
    color='black',
    ax=ax[1],
)
sns.lineplot(
    x='ObservationDate',
    y='Recovered',
    data=poland_data,
    label='Wyzdrowienia',
    color='green',
    ax=ax[1]
)

# Poprawienie wizualizacji
figure.suptitle('Koronawirus w Polsce')
ax[0].set_xlabel('')
ax[1].set_xlabel('Data obserwacji')
ax[0].set_ylabel('Ilość osób')
ax[1].set_ylabel('Ilość osób')
ax[0].get_xaxis().set_ticks([])
plt.setp(ax[1].get_xticklabels(), rotation=45)