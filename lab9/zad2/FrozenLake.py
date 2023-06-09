import gym
import numpy as np
import pygad
import time
from pygad import gann

# Left,Down,Right,Up
gene_space = [0, 1, 2, 3]
moves = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}

S = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 0, 0, 1, 0, 0, 0, 0, 9],
    [9, 0, 0, 0, 0, 0, 1, 0, 0, 9],
    [9, 0, 0, 0, 1, 0, 0, 0, 0, 9],
    [9, 0, 1, 1, 0, 0, 0, 1, 0, 9],
    [9, 0, 1, 0, 0, 1, 0, 1, 0, 9],
    [9, 0, 0, 0, 1, 0, 0, 0, 5, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]


def fitness_func(solution, solution_idx):
    fitness = 0
    squares_visited = set()

    starting_position = (1, 1)
    ending_position = (8, 8)

    current_position = starting_position
    squares_visited.add(current_position)

    for gene in solution:
        previous_position = current_position
        current_position = (
            current_position[0] + moves[gene][0],
            current_position[1] + moves[gene][1],
        )
        (current_position_y, current_position_x) = current_position
        if any(
            [
                current_position_x < 0,
                current_position_x >= len(S[0]),
                current_position_y < 0,
                current_position_y >= len(S),
            ]
        ):
            return 0

        if S[current_position_y][current_position_x] == 1:
            fitness -= 300
            current_position = previous_position
        elif S[current_position_y][current_position_x] == 9:
            fitness -= 1000
        else:
            if current_position == ending_position:
                fitness += 1500
                break
            if current_position in squares_visited:
                fitness -= 50
            else:
                fitness += 20
        squares_visited.add(current_position)
    return fitness


fitness_function = fitness_func
sol_per_pop = 1000
num_genes = 14
num_parents_mating = 10
num_generations = 200
keep_parents = 8
# sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 10

ga_instance = pygad.GA(
    gene_space=gene_space,
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    fitness_func=fitness_function,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    parent_selection_type=parent_selection_type,
    keep_parents=keep_parents,
    crossover_type=crossover_type,
    mutation_type=mutation_type,
    mutation_percent_genes=mutation_percent_genes,
)

# uruchomienie algorytmu
start = time.time()
print("hello")

ga_instance.run()
# print(ga_instance.generations_completed)

end = time.time()
print(end - start)

# podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(solution)
# Best fitness is 1760
print(solution_fitness)

# tutaj dodatkowo wyswietlamy sume wskazana przez jedynki
# THESE LINES BELOW BUG THE CODE
# prediction = numpy.sum(S*solution)
# print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))

# wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
# ga_instance.plot_fitness()

env = gym.make("FrozenLake8x8-v1", render_mode="human", is_slippery=False)


observation, info = env.reset()

for move in solution:
    #  action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(int(move))

    if terminated or truncated:
        observation, info = env.reset()
env.close()
