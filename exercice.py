#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn as sns


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

#methode de monte carlo calcul de pi
#1. creer le cercle


N = 2000  #nombre de points au total

inside = []
outside = []
ligne = []
for i in range(N):
    x = np.random.uniform(0, 1)
    y = np.random.uniform(0, 1)

    if np.sqrt([np.power(x,2) + np.power(y,2)])[0] < 1:
        inside.append((x,y))
    if np.sqrt([np.power(x, 2) + np.power(y, 2)])[0] == 1:
        ligne.append((x,y))
    if np.sqrt([np.power(x, 2) + np.power(y, 2)])[0] > 1:
        outside.append((x,y))

Calcul_pi = 4 * ((len(inside) + len(ligne))/N)

print(f"Pi : {Calcul_pi}")

#graphique

plt.title("Calcul de pi par la méthode de Monte Carlo")
plt.xlim(0, 1)
plt.ylim(0, 1)

plt.scatter(*zip(*inside), color="blue")
plt.scatter(*zip(*outside), color="orange")
#plt.plot(*zip(ligne), color="noir")
plt.show()


#x1, y1 = zip(*inside)
#x2, y2 = zip(*outside)
#x3, y3 = zip(*ligne)

#plt.scatter(*(x1,y1), color = "red")
#plt.scatter(*(x2,y2), color = "blue")
#plt.scatter(*(x3,y3), color = "green")


#x2, y2 = zip(*outside)
#x3, y3 = zip(*ligne)

#plt.scatter((x1,y1), color="blue")
#plt.scatter((x2,y2), color = "orange")
#plt.plot(*zip(*ligne), color = "noir")







if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(linear_values())
    print(coordinate_conversion(np.array([(0, 0), (10, 10), (2, -1)])))
    print(find_closest_index(values=np.array([1, 3, 8, 10]), number=9.5))


    pass
