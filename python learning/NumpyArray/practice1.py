height = [1.7,1.8,1,1.11]
weight =[50,80,70,70]

import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))

bmi = np_weight/np_height **2

print(bmi[bmi > 23])

weights_kg = [5,7,8,9]

np_weights_kg = np.array(weights_kg )

np_weights_lb = np_weights_kg * 2.2

print(np_weights_lb)