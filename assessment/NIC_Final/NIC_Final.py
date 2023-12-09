from tqdm import tqdm
import numpy as np
import random
import matplotlib.pyplot as plt
import datetime
import time

with open("a280-n1395.txt", "r") as f:
    lines = f.readlines()

# print(lines[0])
dimension = int(lines[2].split(":")[1].strip())
num_items = int(lines[3].split(":")[1].strip())
capacity = float(lines[4].split(":")[1].strip())
min_speed = float(lines[5].split(":")[1].strip())
max_speed = float(lines[6].split(":")[1].strip())
renting_ratio = float(lines[7].split(":")[1].strip())
print("Problem Parameters:")
print("Dimension:", dimension)
print("Number of Items:", num_items)
print("Capacity of Knapsack:", capacity)
print("Min Speed:", min_speed)
print("Max Speed:", max_speed)
print("Renting Ratio:", renting_ratio)

items_section_started = False
nodes_section_started = False
coordinates = []
details = []
for line in tqdm(lines, desc='import data'):
    line = line.strip()
    if line.startswith("NODE_COORD_SECTION"):
        nodes_section_started = True
        continue
    elif line.startswith("ITEMS SECTION"):
        items_section_started = True
        nodes_section_started = False
        continue
    elif nodes_section_started and line:
        data = line.split()
        coordinates.append([int(data[0]), int(data[1]), int(data[2])])
    elif items_section_started and line:
        data = line.split()
        details.append([int(data[0]), int(data[1]), int(data[2]), int(data[3])])
coordinates = np.array(coordinates)
details = np.array(details)


def initial_0_1_tags(seed_number):
    details_classifier_f = [[[], []] for _ in range(dimension)]
    details_0_1tag_f = [[] for _ in range(dimension)]
    details_classifier_f[0] = [[0], [0]]
    details_0_1tag_f[0] = [0]
    for i in range(num_items):
        details_classifier_f[details[i, 3] - 1][0].append(details[i, 1])
        details_classifier_f[details[i, 3] - 1][1].append(details[i, 2])

    for i in range(1, dimension):
        random.seed(seed_number + i)
        details_0_1tag_f[i] += ([random.choice([0, 1]) for _ in range(len(details_classifier_f[i][0]))])
    details_classifier_f = np.array(details_classifier_f, dtype=object)
    details_0_1tag_f = np.array(details_0_1tag_f, dtype=object)
    return details_classifier_f, details_0_1tag_f


# 1. Generate an initial population of p randomly created solutions and assess the fitness of each individual in
# the population.
# Give a seed so that the random value returned each time is fixed
# The first column is the path, and the second column is the sum of the distances along the path.
def initial(list_range):
    p = np.zeros((list_range, 4), dtype=object)
    for i, j in tqdm(zip(range(list_range), range(2023, 2023 + population_size), ), total=list_range, desc='initial '
                                                                                                           'population'):
        random.seed(j)
        initial_list = list(range(1, dimension))
        random.shuffle(initial_list)
        p[i, 0] = initial_list
        p[i, 1] = CountF(initial_list)
        p[i, 2],p[i, 3]= CountC(initial_list)
    return p


def distance_matrix_function():
    dm = np.zeros((dimension, dimension))
    for i in tqdm(range(dimension), desc='prepare for matrix distance'):
        for j in range(dimension):
            dm[i, j] = np.sqrt(np.sum(
                (np.array([coordinates[i, 1], coordinates[i, 2]], dtype=float) - np.array(
                    [coordinates[j, 1], coordinates[j, 2]], dtype=float)) ** 2))
    return dm


# compute fitness of every route
# The method is to traverse the array data,
# and add the distance between the last city and the first city
def CountF(p_list):
    s = 0
    if UseDistanceMatrix:
        for i in range(dimension - 2):
            s += distance_matrix[p_list[i], p_list[i + 1]]
        s += distance_matrix[p_list[-1], p_list[0]]
        return s
    else:
        for i in range(dimension - 2):
            s += np.sqrt(
                np.sum((np.array([coordinates[p_list[i], 1], coordinates[p_list[i], 2]], dtype=float) - np.array(
                    [coordinates[p_list[i + 1], 1], coordinates[p_list[i + 1], 2]], dtype=float)) ** 2))
        s += np.sqrt(np.sum((np.array([coordinates[p_list[-1], 1], coordinates[p_list[-1], 2]], dtype=float) - np.array(
            [coordinates[0, 1], coordinates[0, 2]], dtype=float)) ** 2))
        s += np.sqrt(np.sum((np.array([coordinates[0, 1], coordinates[0, 2]], dtype=float) - np.array(
            [coordinates[p_list[0], 1], coordinates[p_list[0], 2]], dtype=float)) ** 2))
        return s


def CountC(p_list):
    # v=v(max)-w/q(v(max)-v(min))
    if UseDistanceMatrix:
        w = 0
        q = capacity
        v = max_speed
        profit = 0
        cost = (distance_matrix[0, p_list[0]] / v) * renting_ratio
        for i in range(1, dimension - 1):  # not include city1 (1 to dimension-2)(0 in this list)
            cur = p_list[i]
            for j in range(len(details_classifier[cur, 0])):
                if details_0_1tag[cur][j] == 1:
                    profit += details_classifier[cur, 0][j]
                    w += details_classifier[cur, 1][j]
                else:
                    continue
            if w >= q:
                v = min_speed
            else:
                v = max_speed - (w / q) * (max_speed - min_speed)
            cost += (distance_matrix[i, i + 1] / v) * renting_ratio
        cost += (distance_matrix[p_list[-1], 0] / v) * renting_ratio
        return profit-cost,profit


# 2. Use tournament selection twice to select two parents, denoted as a and b


# Select random numbers within the number of tournament_size non-repeating populations in the population,
# and select the one with the best result to return
def Tournament_Selection(p_list, count):
    random_t_1 = np.random.choice(population_size, count, replace=False)
    selected_values = population[random_t_1, 1]
    min_index = int(random_t_1[np.argmin(selected_values)])
    res_a = p_list[min_index, 0]

    np.random.seed(seed + np.random.choice(population_size, 1))
    random_t_2 = np.random.choice(population_size, count, replace=False)
    selected_values = population[random_t_2, 1]
    min_index = int(random_t_1[np.argmin(selected_values)])
    res_b = p_list[min_index, 0]
    return res_a, res_b


# 3. apply a Crossover_with_fix on these selected parents to generate two children, referred to as c and d.
# First select a random number so that the two subsets are truncated
# from the index of that number and exchange each other's data.
# When exchanging data here,
# pay attention to whether the values corresponding to the same index between a and b are equal.
# If they are not equal, it means there will be duplication. The duplicate data in c and d must be replaced.
def Crossover_with_fix(kid_a, kid_b):
    random_single_point = int(np.random.choice(dimension - 1))
    kid_c = kid_a[:random_single_point] + kid_b[random_single_point:]
    kid_d = kid_b[:random_single_point] + kid_a[random_single_point:]
    for j in range(random_single_point, dimension - 1):
        if kid_b[j] != kid_a[j]:
            kid_c[kid_c.index(kid_b[j])] = kid_a[j]
            kid_d[kid_d.index(kid_a[j])] = kid_b[j]
    return kid_c, kid_d


# 3. apply a OrderedCrossover on these selected parents to generate two children, referred to as c and d.
# Exchange data first, then add unique data later
def OrderedCrossover(kid_a, kid_b):
    random_single_point = int(np.random.choice(dimension - 1))
    kid_c = kid_a[:random_single_point]
    kid_d = kid_b[:random_single_point]
    for j1 in kid_b:
        if j1 not in kid_c:
            kid_c.append(j1)
    for j2 in kid_a:
        if j2 not in kid_d:
            kid_d.append(j2)

    return kid_c, kid_d


# 4. Run a single_swap_mutation on c and d to give two new solutions e and f. Evaluate the fitness of e and f.
# Swap two points
def single_swap_mutation(m_c, m_d):
    random_e = np.random.choice(dimension - 1, 2, replace=False)
    random_f = np.random.choice(dimension - 1, 2, replace=False)
    m_e = m_c.copy()
    m_f = m_d.copy()

    m_e[random_e[0]], m_e[random_e[1]] = m_e[random_e[1]], m_e[random_e[0]]
    m_f[random_f[0]], m_f[random_f[1]] = m_f[random_f[1]], m_f[random_f[0]]

    return m_e, m_f


# 4. Run a inversion on c and d to give two new solutions e and f. Evaluate the fitness of e and f.
# Slice at random values, then flip the data after that
def inversion(m_c, m_d):
    random_e = np.random.choice(dimension - 1)
    random_f = np.random.choice(dimension - 1)
    m_e = m_c.copy()
    m_f = m_d.copy()

    m_e = m_e[:random_e] + list(reversed(m_e[random_e:]))
    m_f = m_f[:random_f] + list(reversed(m_f[random_f:]))
    return m_e, m_f


# 4. Run a multiple_swap_mutation on c and d to give two new solutions e and f. Evaluate the fitness of e and f.
# Swap multiple points
def multiple_swap_mutation(m_c, m_d, count):
    random_e = np.random.randint(0, dimension - 1, count)
    random_f = np.random.randint(0, dimension - 1, count)
    m_e = m_c.copy()
    m_f = m_d.copy()
    for g in range(count // 2):
        m_e[random_e[g]], m_e[random_e[-(g + 1)]] = m_e[random_e[-(g + 1)]], m_e[random_e[g]]
        m_f[random_f[g]], m_f[random_f[-(g + 1)]] = m_f[random_f[-(g + 1)]], m_f[random_f[g]]

    return m_e, m_f


# 5. Run Replace_Weakest function, firstly for e,        then f
# Replace the value of the worst data in the list
def Replace_Weakest(fit_list):
    fit_score = CountF(fit_list)
    sorted_idx = np.argsort(-population[:, 1])
    if fit_score < population[sorted_idx[0], 1]:
        population[sorted_idx[0], 0], population[sorted_idx[0], 1] = fit_list, fit_score


# 5. Run Replace_FirstWeakest function, firstly for e, then f
# Replace the first value lower than the current value
def Replace_FirstWeakest(fit_list):
    fit_score = CountF(fit_list)
    for h in range(population_size):
        if population[h, 1] >= fit_score:
            population[h, 0], population[h, 1] = fit_list, fit_score
            break


result = []
mutation_count_list = []
tournament_size_list = []

seed = 2000  # Seed value for random number generation
mutation_count = 2  # Number of mutation operations if 10 exchange 5 times
tournament_size = 4
population_size = 10
UseDistanceMatrix = True  # Whether to use the distance matrix,
# this is related to the calculation time,the difference in count_F function
if UseDistanceMatrix:
    distance_matrix = distance_matrix_function()

details_classifier, details_0_1tag = initial_0_1_tags(seed)
population = initial(population_size)  # Initialize the population

# Flags for different states
Crossover_with_fix_state = False  # Whether to enable Crossover_with_fix
OrderedCrossover_state = True  # Whether to enable OrderedCrossover
single_swap_mutation_state = False  # Whether to enable single swap mutation
inversion_state = True  # Whether to enable inversion mutation
multiple_swap_mutation_state = False  # Whether to enable multiple swap mutation
Replace_FirstWeakest_state = True  # Whether to enable replacing the first weakest individual
Replace_Weakest_state = False  # Whether to enable replacing the weakest individual

use_cross = True  # Whether use crossover
save_pic_state = False  # Whether save picture

start_time = time.time()
steps = 10000
# start to loop
for step in tqdm(range(steps), desc='start loop'):
    np.random.seed(seed)
    # if step == 2000:
    #     mutation_count = 6
    # if step == 6000:
    #     mutation_count = 2
    # if step == 6000:
    #     tournament_size = 6
    a, b = Tournament_Selection(population, tournament_size)
    if use_cross:
        if Crossover_with_fix_state:
            c, d = Crossover_with_fix(a, b)
        if OrderedCrossover_state:
            c, d = OrderedCrossover(a, b)
    if not use_cross:
        c, d = a.copy(), b.copy()
    if single_swap_mutation_state:
        e, f = single_swap_mutation(c, d)
    if inversion_state:
        e, f = inversion(c, d)
    if multiple_swap_mutation_state:
        e, f = multiple_swap_mutation(c, d, mutation_count)
    if Replace_FirstWeakest_state:
        Replace_FirstWeakest(e)
        Replace_FirstWeakest(f)
    if Replace_Weakest_state:
        Replace_Weakest(e)
        Replace_Weakest(f)
    score = np.sum(population[:, 1]) / population_size
    result.append(score)
    mutation_count_list.append(mutation_count)
    tournament_size_list.append(tournament_size)
    seed = seed + 1

end_time = time.time()

y = min(population[:, 1])
z = np.argmin(population[:, 1])
x = list(range(0, steps))
current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

print(f'min value is {population[z, 1]}\nthe route is {[0] + population[z, 0]} ')
# Calculate the time difference
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")

plt.figure(figsize=(10, 8))
plt.subplots_adjust(hspace=0.3)

plt.subplot(2, 1, 1)
plt.xlabel('step')
plt.ylabel('sum population cost')
plt.title(f'min_value:{y},m_count:{mutation_count},t_count:{tournament_size},len_p:{population_size}')
plt.plot(x, result, 'r-', lw=3)
plt.legend(['result'])

plt.subplot(2, 2, 3)
plt.plot(x, mutation_count_list, 'g-', lw=3)
plt.xlabel('step')
plt.ylabel('mutation_count')
plt.legend(['mutation_count'])

plt.subplot(2, 2, 4)
plt.plot(x, tournament_size_list, 'b-', lw=3)
plt.xlabel('step')
plt.ylabel('kid_count')
plt.legend(['kid_count'])
if save_pic_state:
    plt.savefig(f'{current_time}.png')
plt.show()
plt.close()

# Print coordinates and item
# print("Node Coordinates:")
# print(coordinates)
# print("\nItem Details:")
# print(details)
# print(population)
# print(population[:, 1])
