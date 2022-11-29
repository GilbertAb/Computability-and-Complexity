from sudoku import Sudoku
import random
import copy

BOARD_SIZE = 9
SUBGRID_SIZE = 3

class SudokuGA:
    def __init__(self, population_size, selection_rate, random_selection_rate,
                num_children, max_num_generations, mutation_rate, model_to_solve,
                presolving, restart_after_n_generations_without_improvement):
        self.population_size = population_size
        self.selection_rate = selection_rate
        self.random_selection_rate = random_selection_rate
        self.num_children = num_children
        self.max_num_generations = max_num_generations
        self.mutation_rate = mutation_rate
        self.model_to_solve = model_to_solve
        self.presolving = presolving
        self.restart_after_n_generations_without_improvement = restart_after_n_generations_without_improvement
        
    def solve(self, sudoku):
        population = self.create_population(sudoku)
        ranked_population = self.fitness(population)
        next_breeders = self.selection(ranked_population)
        new_generation = self.crossover(next_breeders)
        new_generation = self.mutate(new_generation)
    def run(self, sudoku):
        """
        Start the GA to solve the objects
        """
        #values_to_set = self._load().get_initial_values()

        best_data = []
        worst_data = []
        found = False
        overall_num_generations_done = 0
        restart_counter = 0
        population=[]
        while overall_num_generations_done < self.max_num_generations and not found:
            population = self.create_population(sudoku)
            print("Population:", len(population))
            num_generations_done = 0
            remember_the_best = 0
            num_generations_without_improvement = 0

            # Loop until max allowed generations is reached or a solution is found
            while num_generations_done < self.max_num_generations and not found:
                print(num_generations_done)
                # Rank the solutions
                ranked_population = self.fitness(population)
                best_solution = ranked_population[0]
                best_score = best_solution.count_duplicates()

                # Check if problem is solved and print best and worst results
                if best_score > 0:
                    next_breeders = self.selection(ranked_population)
                    new_generation = self.crossover(next_breeders)
                    population = self.mutate(new_generation)
                    num_generations_done += 1
                    overall_num_generations_done += 1
                else:
                    print("Problem solved after {} generations ({} overall generations)!!! Solution found is:".
                          format(num_generations_done, overall_num_generations_done))
                    best_solution.print_solution()
                    found = True

        if not found:
            print("Problem not solved after {} generations. Printing best and worst results below".
                  format(overall_num_generations_done))
            #ranked_population = ga_utils.rank_population(new_population)
            ranked_population = self.fitness(population)
            best_solution = ranked_population[0]
            worst_solution = ranked_population[-1]
            print("Best is:")
            print(best_solution.count_duplicates())
            best_solution.print_solution()
            print("Worst is:")
            worst_solution.print_solution()

        #graphics.draw_best_worst_fitness_scores(best_data, worst_data)

    # Create population
    def create_population(self, sudoku):
        population = []
        for individual in range(self.population_size):
            population.append(self.create_individual(sudoku))
        return population

    def create_individual(self, sudoku):
        individual = Sudoku(sudoku)
        sudoku_solution = individual.solution
        # TODO: avoid duplicated values in 3x3 grid
        #values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        for row in range(BOARD_SIZE):
            for column in range(BOARD_SIZE):
                random_val = random.randrange(1, 10)
                if (individual.sudoku[row][column] == 0):
                    sudoku_solution[row][column] = random_val
                else:
                    sudoku_solution[row][column] = sudoku[row][column]
        individual.solution = sudoku_solution
        return copy.copy(individual)
    
    # Calculate fitness and Order by fitness
    def fitness(self, population):
        individuals_score = {}

        for individual in population:
            individuals_score[individual] = individual.count_duplicates()
        # Highest score (more duplicates) means worst solution
        return sorted(individuals_score, key= individuals_score.get)  

    # Selection
    def selection(self, ranked_population):
        next_breeders = []
        num_best_breeders = int(len(ranked_population) * self.selection_rate)
        num_random_breeders = int(len(ranked_population) * self.random_selection_rate)
        # Keep n best elements
        for i in range(num_best_breeders):
            next_breeders.append(ranked_population[i])
        # Keep randomly n elements
        for i in range(num_random_breeders):
            next_breeders.append(random.choice(ranked_population))
        # Shuffle to avoid keeping only the best at the begining
        random.shuffle(next_breeders)
        return next_breeders
    # Crossover
    # 3x3 grids are the genes for crossover
    def crossover(self, next_breeders):
        next_generation = []
        
        range_val = int(len(next_breeders)/2) * self.num_children
        for i in range(range_val):
            father = random.choice(next_breeders)
            mother = random.choice(next_breeders)
            child = self.create_child(father, mother)
            next_generation.append(child)
        return next_generation
    
    def create_child(self, father, mother):
        # Extract grids
        father_grids = father.get_3x3_subgrids()
        mother_grids = mother.get_3x3_subgrids()

        child = copy.deepcopy(father)
        # Crossover
        crossover_point = random.randrange(1, BOARD_SIZE)
        for i in range(crossover_point):
            # Substitute father's gene with mother's gene
            child.set_3x3_subgrid(mother_grids[i], i)
        return child
    # Mutation
    def mutate(self, next_generation):
        mutated_population = []
        for individual in next_generation:
            if random.random() < self.mutation_rate:
                individual.swap_2_values(random.randrange(0, BOARD_SIZE))
            mutated_population.append(individual)
        return mutated_population

sudo = [
        [8,6,0,2,4,7,5,0,0],
        [7,0,9,1,5,8,6,0,2],
        [2,5,0,9,6,3,1,0,8],
        [9,1,6,0,8,0,0,0,4],
        [0,8,0,0,3,6,9,0,0],
        [0,4,2,7,0,9,0,5,6],
        [0,2,8,0,9,5,4,1,7],
        [4,9,0,8,0,0,0,6,0],
        [0,0,0,6,0,4,3,8,0]]

#pop = create_population(sudo, 5)
ag = SudokuGA(population_size=20, selection_rate=0.25, random_selection_rate=0.25,
            num_children=4, max_num_generations=2000, mutation_rate=0.25, model_to_solve=0,
            presolving=0, restart_after_n_generations_without_improvement=20)
ag.run(sudo)
# Print population
#for i in pop:
#    i.print_solution()
#    i.print_sudoku()
#    print("\n")