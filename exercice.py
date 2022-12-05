#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as plt
import math



# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    Arr = np.linspace(-1.3, 2.5, 64)
    return Arr


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:

    polar = []
    #cartesian_coordinates = np.array([(0, 0), (10, 10), (2, -1)])

    for i in cartesian_coordinates:
        r = np.sqrt(i[0] ** 2 + i[1] ** 2)
        theta = np.arctan2(i[1],i[0])
        polar.append((r, theta))
    #print(polar)

    return np.array(polar)



def find_closest_index(values: np.ndarray, number: float) -> int:
    x = number
    arr = values

    valeur_closest_index = np.absolute(arr-x)
    trouver_index = valeur_closest_index.argmin()
    element = arr[trouver_index]
    index_element = trouver_index


    return trouver_index



#numero avec le graphique:
x = np.linspace(-1,1,250)
#y = x**2 * math.sin(1/(x**2)) + x


y = []
for i in x:
    if i == 0:
        y.append(0)
    else:
        y.append(i ** 2 * math.sin(1 / (i ** 2)) + i)

plt.plot(x,y)
plt.show()


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(linear_values())
    print(coordinate_conversion(np.array([(0, 0), (10, 10), (2, -1)])))
    print(find_closest_index(values=np.array([1, 3, 8, 10]), number=9.5))


    pass
