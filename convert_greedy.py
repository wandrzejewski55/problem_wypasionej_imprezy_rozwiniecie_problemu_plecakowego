#Konwerter danych dla algorytmu zachłannego
#Algorytm przyjmuje dane wejściowe w trochę innej postaci, bo tak było łatwiej go zaimplementować, dlatego zrobiony został konwerter.

from collections import namedtuple
 
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        for i, thing in enumerate(content):
            if i < len(content) - 1:
                file.write(f"{thing},\n")
            else:
                file.write(f"{thing}\n")
 
def transform_to_things(drinks, snacks, meals):
    Thing = namedtuple('Thing', ['name', 'value', 'drink', 'snack', 'meal'])
    things = []
 
    for i in range(len(drinks)):
        guest_name = f'Guest{i + 1}'
        guest_value = 1
        guest_drink = drinks[i]
        guest_snack = snacks[i]
        guest_meal = meals[i]
 
        guest_thing = Thing(guest_name, guest_value, guest_drink, guest_snack, guest_meal)
        things.append(guest_thing)
 
    return things
 
drinks = [9, 9, 7, 3, 1, 2, 8, 1, 10, 1]
snacks = [1, 6, 3, 1, 2, 10, 5, 5, 9, 1]
meals = [3, 5, 4, 3, 6, 6, 3, 9, 4, 6]
drinks_limit = 28
snacks_limit = 23
meals_limit = 30
 
result_content = transform_to_things(drinks, snacks, meals)
 
output_filename = "converted_data.txt"
write_to_file(output_filename, result_content)
 
print(f"Wyniki zostały zapisane do pliku: {output_filename}")



#Dane wyglądają teraz tak:

#Thing(name='Guest1', value=1, drink=9, snack=1, meal=3),
#Thing(name='Guest2', value=1, drink=9, snack=6, meal=5),
#Thing(name='Guest3', value=1, drink=7, snack=3, meal=4),
#Thing(name='Guest4', value=1, drink=3, snack=1, meal=3),
#Thing(name='Guest5', value=1, drink=1, snack=2, meal=6),
#Thing(name='Guest6', value=1, drink=2, snack=10, meal=6),
#Thing(name='Guest7', value=1, drink=8, snack=5, meal=3),
#Thing(name='Guest8', value=1, drink=1, snack=5, meal=9),
#Thing(name='Guest9', value=1, drink=10, snack=9, meal=4),
#Thing(name='Guest10', value=1, drink=1, snack=1, meal=6)
