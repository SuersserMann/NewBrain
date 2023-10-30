import xml.etree.ElementTree as ET
from tqdm import tqdm
import numpy as np
import random
import matplotlib.pyplot as plt
import datetime


# Read the XML file and save the data in NumPy format. Note: one of brazil and burma must be True and the other False.
# Parse the XML file through xml.etree.ElementTree,
# create a numpy array with city_count*city_count dimensions, and save the read data into the array.
def readXml():
    if brazil:
        tree_brazil = ET.parse('brazil58.xml')
        root_brazil = tree_brazil.getroot()
        graph_element_brazil = root_brazil.find('graph')
        city_count_brazil = len(graph_element_brazil.findall('vertex'))
        # make use of a distance matrix denoted as D
        d_brazil = np.zeros((city_count_brazil, city_count_brazil), dtype=object)

        for vertex_idx, vertex_element in enumerate(graph_element_brazil.findall('vertex')):
            for edge_element in vertex_element.findall('edge'):
                cost = edge_element.get('cost')
                city_id = edge_element.text
                d_brazil[vertex_idx, int(city_id)] = float(cost)
        return d_brazil, city_count_brazil
    if burma:
        tree_burma = ET.parse('burma14.xml')
        root_burma = tree_burma.getroot()
        graph_element_burma = root_burma.find('graph')
        city_count_burma = len(graph_element_burma.findall('vertex'))
        # make use of a distance matrix denoted as D
        d_burma = np.zeros((city_count_burma, city_count_burma), dtype=object)

        for vertex_idx, vertex_element in enumerate(graph_element_burma.findall('vertex')):
            for edge_element in vertex_element.findall('edge'):
                cost = edge_element.get('cost')
                city_id = edge_element.text
                d_burma[vertex_idx, int(city_id)] = float(cost)
        return d_burma, city_count_burma


# compute fitness of every route
# The method is to traverse the array data,
# and add the distance between the last city and the first city
def CountF(p_list):
    s = 0
    for i in range(city_count - 1):
        s += data[p_list[i], p_list[i + 1]]
    s += data[p_list[-1], p_list[0]]
    return s


# 1. Generate an initial population of p randomly created solutions and assess the fitness of each individual in
# the population.
# Give a seed so that the random value returned each time is fixed
# The first column is the path, and the second column is the sum of the distances along the path.
def initial(list_range):
    p = np.zeros((list_range, 2), dtype=object)
    for i, j in zip(range(list_range), range(2023, 2023 + population_size)):
        random.seed(j)
        # 给出一个初始化的population
        initial_list = list(range(city_count))
        random.shuffle(initial_list)
        p[i, 0] = initial_list
        p[i, 1] = CountF(initial_list)
    return p


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
    random_single_point = int(np.random.choice(city_count))
    kid_c = kid_a[:random_single_point] + kid_b[random_single_point:]
    kid_d = kid_b[:random_single_point] + kid_a[random_single_point:]
    for j in range(random_single_point, city_count):
        if kid_b[j] != kid_a[j]:
            kid_c[kid_c.index(kid_b[j])] = kid_a[j]
            kid_d[kid_d.index(kid_a[j])] = kid_b[j]
    return kid_c, kid_d


# 3. apply a OrderedCrossover on these selected parents to generate two children, referred to as c and d.
# Exchange data first, then add unique data later
def OrderedCrossover(kid_a, kid_b):
    random_single_point = int(np.random.choice(city_count))
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
    random_e = np.random.choice(city_count, 2, replace=False)
    random_f = np.random.choice(city_count, 2, replace=False)
    m_e = m_c.copy()
    m_f = m_d.copy()

    m_e[random_e[0]], m_e[random_e[1]] = m_e[random_e[1]], m_e[random_e[0]]
    m_f[random_f[0]], m_f[random_f[1]] = m_f[random_f[1]], m_f[random_f[0]]

    return m_e, m_f


# 4. Run a inversion on c and d to give two new solutions e and f. Evaluate the fitness of e and f.
# Slice at random values, then flip the data after that
def inversion(m_c, m_d):
    random_e = np.random.choice(city_count)
    random_f = np.random.choice(city_count)
    m_e = m_c.copy()
    m_f = m_d.copy()

    m_e = m_e[:random_e] + list(reversed(m_e[random_e:]))
    m_f = m_f[:random_f] + list(reversed(m_f[random_f:]))
    return m_e, m_f


# 4. Run a multiple_swap_mutation on c and d to give two new solutions e and f. Evaluate the fitness of e and f.
# Swap multiple points
def multiple_swap_mutation(m_c, m_d, count):
    random_e = np.random.randint(0, city_count, count)
    random_f = np.random.randint(0, city_count, count)
    m_e = m_c.copy()
    m_f = m_d.copy()
    for g in range(count // 2):
        m_e[random_e[g]], m_e[random_e[-(g + 1)]] = m_e[random_e[-(g + 1)]], m_e[random_e[g]]
        m_f[random_f[g]], m_f[random_f[-(g + 1)]] = m_f[random_f[-(g + 1)]], m_f[random_f[g]]

    return m_e, m_f


# 5. Run Replace_Weakest function, firstly for e, then f
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
mutation_count = 6  # Number of mutation operations if 10 exchange 5 times
tournament_size = 4
population_size = 10

brazil = False  # Flag for using Brazil data
burma = True  # Flag for using Burma data
data, city_count = readXml()  # Read data from XML files and get the city count
population = initial(population_size)  # Initialize the population

# Flags for different states
Crossover_with_fix_state = True  # Whether to enable Crossover_with_fix
OrderedCrossover_state = False  # Whether to enable OrderedCrossover
single_swap_mutation_state = False  # Whether to enable single swap mutation
inversion_state = False  # Whether to enable inversion mutation
multiple_swap_mutation_state = True  # Whether to enable multiple swap mutation
Replace_FirstWeakest_state = True  # Whether to enable replacing the first weakest individual
Replace_Weakest_state = False  # Whether to enable replacing the weakest individual
use_cross = True  # Whether use crossover

# start to loop
for step in tqdm(range(10000)):
    np.random.seed(seed)
    if step == 4000:
        mutation_count = 4
    if step == 6000:
        mutation_count = 2
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

y = min(population[:, 1])
z = np.argmin(population[:, 1])
x = list(range(0, 10000))
current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

plt.figure(figsize=(10, 8))
plt.subplots_adjust(hspace=0.3)
city = ""
if brazil:
    city = "Brazil"
elif burma:
    city = "Burma"
plt.subplot(2, 1, 1)
plt.xlabel('step')
plt.ylabel('sum population cost')
plt.title(f'city:{city},min_value:{y},m_count:{mutation_count},t_count:{tournament_size},len_p:{population_size}')
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
plt.savefig(f'{city}_{current_time}.png')
plt.show()
plt.close()
print(f'min value of {city} is {population[z, 1]}\nthe route is {population[z, 0]} ')
