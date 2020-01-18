import csv
import networkx as nx
from myFunc import *


def my_degreedist(fin_gexf, tag_PR):
    tag_ALGO = 'degree_distribution'

    list_degree = []
    dict_degree = {}
    G = nx.read_gexf(fin_gexf)

    for node in list(G.nodes()):
        degree = G.degree(node, weight='weight')
        list_degree.append(degree)
        if degree in dict_degree.keys():
            dict_degree[degree] = dict_degree[degree] + 1
        else:
            dict_degree[degree] = 1

    fout_png = 'output/pic/' + tag_PR + '_' + tag_ALGO + '_log' + '.png'
    tag_title = tag_PR + ': Degree Distribution'
    tag_x = 'Degree'
    tag_y = 'Probability'

    my_scatterplot(list(dict_degree.keys()), list(dict_degree.values()), tag_title, tag_x, tag_y, fout_png, True)

    fout_png = 'output/pic/' + tag_PR + '_' + tag_ALGO + '_hist' + '.png'
    my_plothist(list_degree, tag_title + 'Histogram:', 'Degree k', 'Portion of node Pk', fout_png)

    return True
