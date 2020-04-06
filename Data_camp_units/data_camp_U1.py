# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd

heights_in = pd.read_csv('/Users/brett/Documents/sandbox/heights_weights.csv', index_col = "Name")

print(heights_in)

np_height_in = np.array(heights_in)

print(np_height_in[:,3] * 0.0254)

print(180.0 * 0.0254)

height = np_height_in[:,2] * 0.0254
weight = np_height_in[:,3] * 0.4534
bmi = weight/height**2

print(bmi)

light = bmi < 21

print(light)

print(bmi[light])

print(bmi.shape)








