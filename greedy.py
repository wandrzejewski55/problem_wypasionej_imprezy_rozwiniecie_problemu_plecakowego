#Algorytm zachłanny
#Algorytm sortuje indeksy gości na podstawie współczynnika, który uwzględnia sumę wartości napojów, przekąsek i dań dla każdego gościa.
#Następnie, iterując po posortowanych gościach, dodaje ich do zestawienia, sprawdzając jednocześnie, czy nie przekracza limitów zasobów. Algorytm nie zawsze gwarantuje optymalności, co oznacza, że istnieje ryzyko pominięcia bardziej korzystnych kombinacji gości.

def greedy(drinks, snacks, meals, drinks_limit, snacks_limit, meals_limit):
 
    sorted_indices = set_coef(drinks,snacks, meals)
    value_with_current_guest = 0
    guests_with_current = []
    for i in range(len(drinks)):
        if drinks_limit >= drinks[sorted_indices[i]] and snacks_limit >= snacks[sorted_indices[i]] and meals_limit >= meals[sorted_indices[i]]:
            value_with_current_guest += 1
            guests_with_current.append(sorted_indices[i])
            drinks_limit -= drinks[sorted_indices[i]]
            snacks_limit -= snacks[sorted_indices[i]]
            meals_limit -= meals[sorted_indices[i]]
 
 
 
    return value_with_current_guest, guests_with_current
 
 
 
def set_coef(drinks, snacks, meals):
    n = len(drinks)
    coefficients = []
    temp = 0
    indices = list(range(n))
 
    for i in range(n):
        temp = drinks[i] + snacks[i] + meals[i]
        coefficients.append(temp)
        temp = 0
 
 
    sorted_indices = sorted(indices, key=lambda x: coefficients[x])
 
 
    return sorted_indices
