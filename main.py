import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2
import sys

# Testv2.csv - Volume
# World-Stock-Prices-Dataset.csv - Volume

# avocado.csv - Total Volume
# creditcard_2023.csv - Amount
# salary_data.csv - highest_salary
# housing.csv - median_house_value
# onlinefraud.csv - amount


# Wgranie zestawu danych
df = pd.read_csv('C:/Users/aga54/Desktop/Praca_inżynierska/avocado.csv')
data = df['Total Volume']
df.isnull().sum()


# Wartość oczekiwana (teoretyczna)
total_rows = df.shape[0]    # zliczanie wierszy
Benford = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
expected_counts = np.array([round(p * total_rows / 100) for p in Benford])
print("Warość oczekiwana:", expected_counts)


# Wartość mierzona (empiryczna)
fd_data = data.astype(str).str[:1].astype(int)
digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
observed_counts = np.array([fd_data.value_counts()[i] for i in digit])
print("Warość mierzona:", observed_counts)

#Rozkład empiryczny (mierzony)
measured_distribution = (observed_counts/total_rows)*100
# print(measured_distribution)


# Obliczenia dla testu Chi-kwadrat
chi2_stat = np.sum((measured_distribution - Benford)**2 / Benford)  # * total_rows ??

# Stopnień swobody
degrees_of_freedom = len(digit) - 1

# Wartość p
p_value = 1 - chi2.cdf(chi2_stat, degrees_of_freedom)

# Wyniki testu Chi-kwadrat
print()
print("Wyniki testu Chi-kwadrat:")
print("Wartość statystyki Chi-kwadrat:", chi2_stat)
print("Wartość p:", p_value)


# Średnie odchylenie bezwzględne
mad = ((np.sum(abs(measured_distribution - Benford)))/9)
print("Średnie odchylanie bezwzględne: ", mad)


# Dywergencja Kullbacka-Leiblera
divKL = np.sum(measured_distribution * abs(np.log2(measured_distribution/Benford)))
print("Dywergencja Kullbacka-Leiblera: ", divKL)


# Rysowanie wykresu
plt.bar(digit, observed_counts, label='Rozkład pierwszych cyfr')    # , color='#73b3bb'
plt.plot(digit, expected_counts, label='Rozkład Benforda', color='orangered')   # color='#737373'
plt.xlabel('Cyfra')
plt.ylabel('Liczba wystąpień')
plt.title('Porównanie Rozkładu Benforda z danymi rzeczywistymi')
plt.legend()
plt.show()