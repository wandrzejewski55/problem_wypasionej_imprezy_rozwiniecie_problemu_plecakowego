#Algorytm genetyczny
#Algorytm genetyczny działa tak, że na początku tworzy zestaw randomowych rozwiązań dla każdego rozwiązania liczony jest współczynnik fitness, czyli jak dobre jest rozwiązanie. Następnie następuje selekcja, 
#gdzie do następnej generacji wybierane na wybranie mają większe szanse genomy z większym współczynnikiem fitness. Pomiędzy tymi genomami następuje łączenie. Jest losowo wybierana liczba p, 
#względem której będą podzielone te dwie tablice z rozwiązaniami, następnie, następuje wymieszanie. Kolejnym etapem jest mutacja, gdzie również losowo odbywa zmiana się bitu poszczególnego genomu. Całe postępowanie wykonywane jest przez określoną liczbę generacji.

from typing import List, Callable, Tuple
from random import choices, random, randint, randrange
from collections import namedtuple
from functools import partial
 
Thing = namedtuple('Thing', ['name', 'value', 'drink', 'snack', 'meal'])
things = [
Thing(name='Guest1', value=1, drink=2, snack=3, meal=4),
Thing(name='Guest2', value=1, drink=3, snack=7, meal=5),
Thing(name='Guest3', value=1, drink=8, snack=1, meal=2),
Thing(name='Guest4', value=1, drink=10, snack=7, meal=8),
Thing(name='Guest5', value=1, drink=4, snack=8, meal=9),
Thing(name='Guest6', value=1, drink=3, snack=4, meal=5),
Thing(name='Guest7', value=1, drink=7, snack=6, meal=3),
Thing(name='Guest8', value=1, drink=9, snack=3, meal=10),
Thing(name='Guest9', value=1, drink=9, snack=2, meal=10),
Thing(name='Guest10', value=1, drink=6, snack=7, meal=3),
]
 
Genome = List[int]
Population = List[Genome]
FitnessFunc = Callable[[Genome], int]
PopulateFunc = Callable[[], Population]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]
 
 
def generate_genome(length: int) -> Genome:
    return choices([0,1], k=length)
 
def generate_population(size: int, genome_length: int) -> Population:
    return [generate_genome(genome_length) for _ in range(size)]
 
 
def fitness(genome: Genome, things: [Thing], drinks_limit: int, snacks_limit: int, meals_limit: int) -> int:
    if len(genome) != len(things):
        raise ValueError("Wrong length of genome!")
 
    drinks = 0
    snacks = 0
    meals = 0
    value = 0
 
    for i, thing in enumerate(things):
        if genome[i] == 1:
            drinks += thing.drink
            snacks += thing.snack
            meals += thing.meal
            value += thing.value
 
            if (drinks_limit < drinks) or (snacks_limit < snacks) or (meals_limit < meals):
                return 0
 
    return value
 
def selection_pair(population: Population, fitness_func: FitnessFunc) -> Population:
    return choices(
        population=population,
        weights= ((fitness_func(genome) for genome in population)),
        k=2
    )
 
 
def single_point_crossover(a:Genome, b:Genome) -> Tuple[Genome, Genome]:
    if len(a) != len(b):
        raise ValueError("genomes not equal")
 
    length = len(a)
    if length < 2:
        return a, b
    p = randint(0, length -1)
    return a[0:p] + b[p:], b[0:p] + a[p:]
 
 
def mutation(genome: Genome, num: int=1, probability: float=0.5 , ) -> Genome:
    for _ in range(num):
        index = randrange(len(genome))
        genome[index] = genome[index] if random() > probability else abs(genome[index] - 1)
 
    return genome
 
 
 
 
def run_evolution(
        populate_func: PopulateFunc,
        fitness_func: FitnessFunc,
        fitness_limit: int,
        selection_func: SelectionFunc = selection_pair,
        crossover_func: CrossoverFunc = single_point_crossover,
        mutation_func: MutationFunc = mutation,
        generation_limit: int= 100
) -> Tuple[Population, int]:
    population = populate_func()
 
    for i in range(generation_limit):
        population = sorted(
            population,
        key=lambda genome: fitness_func(genome),
            reverse=True
        )
 
        if fitness_func(population[0]) >= fitness_limit:
            break
 
        next_generation = population[0:2]
 
 
        for j in range(int (len(population) /2 ) - 1 ):
            parents = selection_func(population, fitness_func)
            offspring_a, offspring_b = crossover_func(parents[0], parents[1])
            offspring_a = mutation_func(offspring_a)
            offspring_b = mutation_func(offspring_b)
            next_generation += [offspring_a, offspring_b]
 
        population = next_generation
 
    population = sorted(
        population,
        key= lambda genome: fitness_func(genome),
        reverse=True
    )
 
    return population, i
