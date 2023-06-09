import gym
import numpy as np
import pygad
from pygad import gann

# Left,Down,Right,Up
gene_space = [0, 1, 2, 3]

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

fitness_function = fitness_func
# ile chromsomów w populacji
# ile genow ma chromosom
sol_per_pop = 10
num_genes = len(S)
# ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
# ile pokolen
# ilu rodzicow zachowac (kilka procent)
num_parents_mating = 5
num_generations = 30
keep_parents = 2
# jaki typ selekcji rodzicow?
# sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"
# w il =u punktach robic krzyzowanie?
crossover_type = "single_point"
# mutacja ma dzialac na ilu procent genow?
# trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 10

# env = gym.make("FrozenLake8x8-v1", render_mode="human", is_slippery=False)


# observation, info = env.reset()

# for _ in range(14):
#     #  action = env.action_space.sample()
#     observation, reward, terminated, truncated, info = env.step(1)

#     if terminated or truncated:
#         observation, info = env.reset()
# env.close()
