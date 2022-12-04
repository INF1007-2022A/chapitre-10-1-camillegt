#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np




# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    Arr = np.linspace(-1.3, 2.5, 64)
    return Arr


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:

    polar = []
    cartesian_coordinates = np.array([(0, 0), (10, 10), (2, -1)])

    for i in cartesian_coordinates:
        for j in i:
            r = np.sqrt(j[0] ** 2 + j[1] ** 2)
            teta= np.arctan2(j[1],j[0])
            polar.append((r, teta))
    print(polar)

    #return np.array([polar])



def find_closest_index(values: np.ndarray, number: float) -> int:
    x = number
    arr = values

    valeur_closest_index = np.absolute(arr-x)
    trouver_index = valeur_closest_index.argmin()
    element = arr[trouver_index]
    index_element = trouver_index


    return trouver_index


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(linear_values())
    print(coordinate_conversion())
    print(find_closest_index(values=np.array([1, 3, 8, 10]), number=9.5))


    pass
