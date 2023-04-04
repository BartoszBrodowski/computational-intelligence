import numpy as np
import pygad

class CustomGA(pygad.GA):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def custom_crossover(parent1, parent2):
        parent1_board = parent1.reshape((9, 9))
        parent2_board = parent2.reshape((9, 9))

        offspring1_board = parent1_board.copy()
        offspring2_board = parent2_board.copy()

        # Choose a random number of rows to exchange between the two parents
        num_rows_to_exchange = np.random.randint(1, 5)

        # Randomly select rows to exchange
        rows_to_exchange = np.random.choice(9, num_rows_to_exchange, replace=False)

        for row in rows_to_exchange:
            offspring1_board[row, :] = parent2_board[row, :]
            offspring2_board[row, :] = parent1_board[row, :]

        return offspring1_board.flatten(), offspring2_board.flatten()
    
    def crossover(self, parent1, parent2):
        return self.custom_crossover(parent1, parent2)

    def custom_mutation(self, offspring):
        offspring_board = offspring.reshape((9, 9))

        # Choose a random row to mutate
        row_idx = np.random.randint(0, 9)

        # Get the unique values in the row and shuffle them, excluding the initial board values
        unique_row_values = np.unique(offspring_board[row_idx, initial_board[row_idx] == 0])
        np.random.shuffle(unique_row_values)

        # Assign the shuffled values back to the row, excluding the initial board values
        offspring_board[row_idx, initial_board[row_idx] == 0] = unique_row_values

        return offspring_board.flatten()

    def mutation(self, offspring):
        return self.custom_mutation(offspring)

# Define the gene space
gene_space = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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

    for row in board:
        unique_row = np.unique(row)
        fitness += (9 - len(unique_row)) * 3

    for j in range(9):
        column = []
        for i in range(9):
            column.append(board[i][j])
        unique_column = np.unique(column)
        fitness += (9 - len(unique_column)) * 2

    for box_i in range(3):
        for box_j in range(3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(board[3*box_i + i][3*box_j + j])
            unique_subgrid = np.unique(subgrid)
            fitness += (9 - len(unique_subgrid)) * 1

    for i in range(9):
        for j in range(9):
            if initial_board[i][j] != 0 and board[i][j] != initial_board[i][j]:
                fitness -= 20

    return -fitness


# Create an instance of the GA class inside the ga module. Some parameters are initialized within the constructor.
ga_instance = CustomGA(
    initial_population=None,
    num_generations=1000,
    num_parents_mating=10,
    fitness_func=fitness_function,
    sol_per_pop=120,
    num_genes=81,
    gene_space=gene_space,
    init_range_low=1,
    init_range_high=9,
    mutation_probability=0.04,
    parent_selection_type="sss"
)

# Run the GA to compute the solution
ga_instance.run()

# After the generations complete, some plots are showed that summarize how the outputs/fitness values evolve over generations.
ga_instance.plot_fitness()

# Retrieve the best solution after training the GA.
solution, solution_fitness, solution_idx = ga_instance.best_solution()

# Print the solution and solution's fitness
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

# Reshape the solution into a 9x9 grid
board = solution.reshape((9, 9))

# Print the board
print(board)