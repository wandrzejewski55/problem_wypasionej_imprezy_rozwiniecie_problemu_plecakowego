#Algorytm siłowy (wersja rekurencyjna)
#Funkcja brute_force rekurencyjnie przeszukuje wszystkie możliwe kombinacje gości, starając się znaleźć optymalne rozwiązanie spełniające limity zasobów. To proste, ale kosztowne obliczeniowo podejście, które może być nieefektywne dla dużych zbiorów danych.

def brute_force(drinks, snacks, meals, drinks_limit, snacks_limit, meals_limit, n):
 
    if n == 0 or drinks_limit == 0 or snacks_limit == 0 or meals_limit == 0:
        return 0, []
 
    if drinks[n-1] > drinks_limit or snacks[n-1] > snacks_limit or meals[n-1] > meals_limit:
        return brute_force(drinks, snacks, meals, drinks_limit, snacks_limit, meals_limit, n - 1)
 
 
    else:
 
        value_with_current_guest, guests_with_current = brute_force(
            drinks, snacks, meals,
            drinks_limit - drinks[n-1], snacks_limit - snacks[n-1], meals_limit - meals[n-1],
            n - 1
        )
        value_with_current_guest += 1
 
        value_without_current_guest, guests_without_current = brute_force(
            drinks, snacks, meals,
            drinks_limit, snacks_limit, meals_limit,
            n - 1
        )
 
        if value_with_current_guest > value_without_current_guest:
            return value_with_current_guest, guests_with_current + [n-1]
        else:
            return value_without_current_guest, guests_without_current





