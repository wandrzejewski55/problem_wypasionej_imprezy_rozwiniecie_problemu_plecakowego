#Algorytm siłowy (wersja iteracyjna)
#Ten algorytm również poszukuje optymalnego zestawienia gości, jednak zastosowano tutaj podejście iteracyjne. Algorytm generuje wszystkie możliwe kombinacje gości, sprawdzając, czy spełniają one limity zasobów. Również nieefektywne dla dużych zbiorów danych.


def iterativeBruteForce(drinks, snacks, meals, drinks_limit, snacks_limit, meals_limit):
    n = len(drinks)
    max_guests = 0
    selected_guests = []
 
    for i in range(1 << n):
        total_drinks = 0
        total_snacks = 0
        total_meals = 0
        total_guests = 0
        current_selection = []
 
        for j in range(n):
            if i & (1 << j):
                current_selection.append(j)
                total_drinks += drinks[j]
                total_snacks += snacks[j]
                total_meals += meals[j]
                total_guests += 1
 
        if (
            total_drinks <= drinks_limit
            and total_snacks <= snacks_limit
            and total_meals <= meals_limit
            and total_guests > max_guests
        ):
            max_guests = total_guests
            selected_guests = current_selection
 
    return max_guests, selected_guests
