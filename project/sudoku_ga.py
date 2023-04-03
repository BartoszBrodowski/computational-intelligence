import numpy as np
import pygad


gene_space = [1,2,3,4,5,6,7,8,9]

# Define the Sudoku board
initial_board = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])


# Define the fitness function
def fitness_function(solution, solution_idx):
    board = solution.reshape((9, 9))
    
    fitness = 0

    # Check rows
    for row in board:
        fitness += 9 - len(np.unique(row))
    # Check columns
    for column in board:
        for j in range(9):
            column = []
            for i in range(9):
                column.append(board[i][j])
        fitness += 9 - len(np.unique(column))
    # Check subgrids
    for box_i in range(3):
        for box_j in range(3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(board[3*box_i + i][3*box_j + j])
        fitness += 9 - len(np.unique(subgrid))
    
    # Check for unchangable genes
    for i in range(9):
        for j in range(9):
            if board[i][j] != initial_board[i][j] and initial_board[i][j] != 0:
                fitness = fitness / 3
                return

    return fitness

ga_instance = pygad.GA(gene_space=gene_space,
                     num_generations=1000, 
                     num_parents_mating=20, 
                     fitness_func=fitness_function,
                     sol_per_pop=200,
                     num_genes=81,
                     parent_selection_type="rank",
                     keep_parents=10,
                     crossover_type="two_points", 
                     mutation_type="random",
                     mutation_percent_genes=5)

ga_instance.run()
solution, solution_fitness, solution_idx = ga_instance.best_solution()

print(solution_fitness)
print(solution.reshape((9, 9)))
