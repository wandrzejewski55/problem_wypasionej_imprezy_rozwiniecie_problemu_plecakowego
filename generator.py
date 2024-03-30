#Losowy generator danych wejściowych
#Generator danych tworzy 3 listy reprezentujące różne aspekty organizacji imprezy, takie jak napoje, przekąski oraz dania.
#Danemu indeksowi na każdej z list odpowiada ten sam gość. Oprócz tego generowane są również limity napoi, przekąsek oraz dań ( impreza ma zasoby, których nie może przekroczyć). Wyniki zapisane są w oddzielnym pliku txt.
import random
 
def generate_guests_data(num_guests):
    drinks = [random.randint(1, 10) for _ in range(num_guests)]
    snacks = [random.randint(1, 10) for _ in range(num_guests)]
    meals = [random.randint(1, 10) for _ in range(num_guests)]
 
    drinks_limit = random.randint(20, 30)
    snacks_limit = random.randint(20, 30)
    meals_limit = random.randint(20, 30)
 
    return drinks, snacks, meals, drinks_limit, snacks_limit, meals_limit
 
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
 
num_guests = 10
output_filename = 'guests_data.txt'
 
drinks, snacks, meals, drinks_limit, snacks_limit, meals_limit = generate_guests_data(num_guests)
 
result_content = f"drinks = {drinks}\nsnacks = {snacks}\nmeals = {meals}\n"
result_content += f"drinks_limit = {drinks_limit}\nsnacks_limit = {snacks_limit}\nmeals_limit = {meals_limit}\n"
 
 
write_to_file(output_filename, result_content)
 
print(f"Wyniki zostały zapisane do pliku: {output_filename}")



#Przykładowy input
#drinks = [2, 3, 8, 10, 4, 3, 7, 9, 9, 6]
#snacks = [3, 7, 1, 7, 8, 4, 6, 3, 2, 7]
#meals = [4, 5, 2, 8, 9, 5, 3, 10, 10, 3]
#drinks_limit = 22
#snacks_limit = 20
#meals_limit = 26





