import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2
import sys

# Testv2.csv - Volume
# avocado.csv - Total Volume
# creditcard_2023.csv - Amount
# salary_data.csv - highest_salary
# World-Stock-Prices-Dataset.csv - Volume
# housing.csv - median_house_value
# onlinefraud.csv - amount - za duża baza ???


# Wgranie zestawu danych
df = pd.read_csv('C:/Users/aga54/Desktop/Praca_inżynierska/avocado.csv')
data = df['Total Volume']
df.isnull().sum()

# Wyliczenie watości oczekiwanej
total_rows = df.shape[0]    # zliczanie wierszy
Benford = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]

expected_counts = np.array([round(p * total_rows / 100) for p in Benford])
print("Warość oczekiwana:", expected_counts)


# Wyliczenie watości mierzonej
fd_data = data.astype(str).str[:1].astype(int)
digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]

observed_counts = np.array([fd_data.value_counts()[i] for i in digit])
print("Warość mierzona:", observed_counts)


# Obliczenia dla testu Chi-kwadrat
chi2_stat = np.sum((observed_counts - expected_counts)**2 / expected_counts)

# Stopnie swobody to liczba kategorii minus 1
degrees_of_freedom = len(digit) - 1

# Wartość p (przy użyciu rozkładu chi-kwadrat)
p_value = 1 - chi2.cdf(chi2_stat, degrees_of_freedom)

# Wyświetlenie wyników testu Chi-kwadrat
print()
print("Wyniki testu Chi-kwadrat:")
print("Wartość statystyki Chi-kwadrat:", chi2_stat)
print("Wartość p:", p_value)


# Rysowanie wykresu
plt.bar(digit, observed_counts, label='Rozkład pierwszych cyfr')    # , color='#73b3bb'
plt.plot(digit, expected_counts, label='Rozkład Benforda', color='orangered')   # color='#737373'
plt.xlabel('Cyfra')
plt.ylabel('Liczba wystąpień')
plt.title('Porównanie Rozkładu Benforda z danymi rzeczywistymi')
plt.legend()
plt.show()