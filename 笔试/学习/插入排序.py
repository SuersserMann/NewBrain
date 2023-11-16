import numpy as np

a_list = np.random.randint(1, 101, 100)
print()


def insert(a_list):
    if len(a_list) == 1:
        return a_list
    else:
        for i in range(len(a_list)):
            while i != 0:
                if a_list[i] < a_list[i - 1]:
                    a_list[i], a_list[i - 1] = a_list[i - 1], a_list[i]
                    i -= 1
                else:
                    break
        return a_list


print(insert(a_list))
