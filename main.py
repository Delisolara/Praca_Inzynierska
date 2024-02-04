import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2
import sys

# Wgranie zestawu danych
df = pd.read_csv('ścieżka_do_zestawu danych')
data = df['nazwa_tabeli']
df.isnull().sum()

total_rows = df.shape[0]   # zliczanie wierszy
benford_type = input("Podaj cyfrę jaką chcesz analizować: ")

def benford_distribution(total_rows,benford_type):
    # Wybór pierwszej lub drugiej cyfry
    if benford_type == '1':
        digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        benford = [0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]
        fd_data = data.astype(str).str[:1].astype(int)
    elif benford_type == '2':
        digit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        benford = [0.12, 0.114, 0.109, 0.104, 0.1, 0.097, 0.093, 0.09, 0.088, 0.085]
        fd_data = data.astype(str).apply(lambda x: int(x[1]) if x[1].isdigit() else 0)
    else:
        raise ValueError("Invalid benford_type. Use '1' or '2'.")

    # Wartość teoretyczna (oczekiwana)
    expected_counts = np.array([round(p * total_rows) for p in benford])
    print("Wartość teoretyczna:", expected_counts)

    # Wartość empiryczna (mierzona)
    observed_counts = observed_counts = np.array([fd_data.value_counts()[i] for i in digit])
    print("Wartość empiryczna:", observed_counts, "\n")

    # Rozkład empiryczny
    measured_distribution = (observed_counts / total_rows)

    # Wartość statystyki Chi-kwadrat
    chi2_stat = (np.sum(((measured_distribution - benford)**2 / benford))) * total_rows

    # Stopnień swobody
    degrees_of_freedom = len(digit) - 1

    # Wartość p
    p_value = 1 - chi2.cdf(chi2_stat, degrees_of_freedom)

    # Wyniki testu Chi-kwadrat
    print("Wyniki testu Chi-kwadrat:")
    print("Wartość statystyki Chi-kwadrat:", chi2_stat)
    print("Wartość p:", p_value, "\n")

    # Średnie odchylenie bezwzględne
    mad = round(((np.sum(abs(measured_distribution - benford)))/9) * 100, 2)
    print("Średnie odchylanie bezwzględne:", mad, "%")

    # Dywergencja Kullbacka-Leiblera
    divKL = np.sum(measured_distribution * abs(np.log2(measured_distribution/benford)))
    print("Dywergencja Kullbacka-Leiblera:", divKL)

    # Rysowanie wykresu
    plt.bar(digit, observed_counts, label='Wartość mierzona', color='#4472c4')
    plt.plot(digit, expected_counts, label='Wartość oczekiwana', color='#ed7d31')

    plt.xlabel('Cyfra')
    plt.ylabel('Liczba wystąpień')
    # plt.title('Porównanie wartości mierzonych z oczekiwanymi')
    plt.legend()
    plt.show()

try:
    result = benford_distribution(total_rows, benford_type)
    print(result)
except ValueError as e:
    print(e)