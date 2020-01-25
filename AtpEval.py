import networkx as nx
from myFunc import *
import numpy as np
import matplotlib.pyplot as plt
import os
my_path = os.path.abspath(__file__)

list_alpha = list()
max_alpha = 1
for i in range(1, 10):
    list_alpha.append(i * 0.1)

print(list_alpha)
print(0.1*3)