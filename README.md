Program pomocniczy użyty w pracy dyplomowej pt. "Zastosowanie prawa Benforda do wykrywania prób manipulacji danymi", który został stworzony w języku Python z wykorzystaniem bibliotek: Pandas, Matplotlib oraz modułu scipy.stats.chi2. Algorytm programu obejmował następujące kroki:
1) Wyliczanie wartości teoretycznych poprzez pomnożenie łącznej liczby wierszy tabeli przez tablicę zawierającą rozkład Benforda (dla pierwszej lub drugiej cyfry).
2) Wyciąganie i zliczanie pierwszych cyfr (wartości empirycznych) z wybranej tabeli w bazie danych.
3) Obliczanie rozkładu empirycznego przez podzielenie wcześniej zliczonych cyfr przez ilość wierszy.
4) Przeprowadzanie testu chi-kwadrat, obliczanie średniego odchylenia bezwzględnego oraz dywergencji Kullbacka-Leiblera.
5) Zwracanie wyników miar i generowanie wykresu zestawiającego wartości pomierzone z wartościami oczekiwanymi.
