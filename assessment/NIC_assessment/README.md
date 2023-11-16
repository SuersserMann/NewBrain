# check environment

- This file requires the import of four additional packages.
Please confirm whether these packages are already configured in your environment.

  `xmltodict==0.13.0`

  `tqdm==4.64.1`

  `numpy==1.23.5`

  `matplotlib==3.7.2`

- Alternatively, you can directly input the following command in PyCharm's Terminal:
  - pip install -r requirements.txt

## Introduction to Parameters

- Starting from line 187 in the code is the section where parameters are set. It is convenient to modify these parameters for different experiments.

- Used to set the random seed.
  
  - `seed = 2000`: 
- Sets the number of mutations.
  - `mutation_count = 2`
- Sets the size of the tournament.
  - `tournament_size = 4`
- Sets the size of the population.
  - `population_size = 10`
  
- Used to determine which city to experiment on. Note that the states of the two cities must be one `True` and the other `False`.

  - `brazil = True`
  
  - `burma = False`

- Determines whether to use `Crossover_with_fix` or `OrderedCrossover`. Note that at least one crossover method should be set to `True`, and the others set to `False`.
  - `Crossover_with_fix_state = False`
  - `OrderedCrossover_state = True`

- Determines whether to use `single_swap_mutation`, `inversion`, or `multiple_swap_mutation`. Note that at least one mutation method should be set to `True`, and the others set to `False`.
  - `single_swap_mutation_state = False`

  - `inversion_state = True`
  
  - `multiple_swap_mutation_state = False`

- Determines whether to use `Replace_FirstWeakest` or `Replace_Weakest`. Note that at least one replacement method should be set to `True`, and the others set to `False`.
  - `Replace_FirstWeakest_state = True`
  - `Replace_Weakest_state = False`

- Specifies whether to use crossover.
  - `use_cross = True`
- Specifies whether to save result images.
  - `save_pic_state = False`

## show results in console
- min value of city
- the route
- Elapsed time
- For example:
  - min value of Brazil is 26494.0
  - the route is [53, 54, 7, 21, 3, 49, 52, 19, 31, 24, 8, 39, 12, 29, 0, 17, 43, 57, 23, 56, 11, 22, 4, 26, 42, 48, 46, 50, 9, 51, 34, 2, 28, 32, 36, 44, 55, 45, 14, 33, 13, 27, 18, 5, 16, 25, 35, 20, 38, 10, 6, 30, 41, 37, 15, 47, 40, 1] 
  - Elapsed time: 1.8578126430511475 seconds