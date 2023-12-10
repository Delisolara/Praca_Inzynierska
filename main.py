import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

# Testv2.csv - Volume
# avocado.csv - Total Volume
# creditcard_2023.csv - Amount
# salary_data.csv - highest_salary
# World-Stock-Prices-Dataset.csv - Volume
# housing.csv - median_house_value
# onlinefraud.csv - amount - za duża baza ???

df = pd.read_csv('C:/Users/aga54/Desktop/Praca_inżynierska/housing.csv')
data = df['median_house_value']
# print(df['Volume'])   #lub print(df.iloc[:,5])

# Wyliczenie wyników na podstawie rozkładu Benforda
total_rows = df.shape[0]    # zliczanie wierszy
Benford = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]

def benford_results(rows):
    print("Wyniki wyliczone na podstawie rozkładu Benforda:")
    for index, p in enumerate(Benford):
        result = round(p * rows / 100)
        print("Cyfra", index + 1, "->", result)

    #Wykres rozkładu Benforda
    # plt.plot(range(1, 10), [round(p * rows / 100) for p in Benford], label='Rozkład Benforda', color='orangered')
    plt.plot(range(1, 10), [round(p * rows / 100) for p in Benford], label='Rozkład Benforda', color='#737373')

    # results = [round(p * rows / 100) for p in Benford]
    # print(results)


# Zliczanie ilości pierwszych cyfr
def first_digit(data):
    fd_data = data.astype(str).str[:1].astype(int)
    digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("Wynik wyliczony z wgranej bazy:")
    for i in digit:
        count_digit = fd_data.value_counts()[i]
        print("Cyfra", i, "->", count_digit)

    # Wykres rozkładu pierwszych cyfr
    # plt.bar(digit, [fd_data.value_counts()[i] for i in digit], label='Rozkład pierwszych cyfr')
    plt.bar(digit, [fd_data.value_counts()[i] for i in digit], label='Rozkład pierwszych cyfr', color='#73b3bb')

    # count = fd_data.value_counts(dropna=False)[3]
    # print(count)


# Wywołanie funkcji
df.isnull().sum()
benford_results(total_rows)
print()
first_digit(data)

plt.xlabel('Cyfra')
plt.ylabel('Liczba wystąpień')
plt.title('Porównanie Rozkładu Benforda z danymi rzeczywistymi')
plt.legend()
plt.show()
