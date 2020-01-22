import csv
import networkx as nx
from myFunc import *


def my_distance_dist(fin_gexf, fout_csv, fout_png_name):

    tag_PR = '2'
    tag_ALGO = 'distance_distribution'

    G = nx.read_gexf(fin_gexf)
    list_node = list(G.nodes())
    first_node = list_node[1]
    list_avgpath = list()

    # degree = G.degree(node)
    with open(fout_csv, 'w', newline='') as outputFile_0:
        write_File_0 = csv.writer(outputFile_0)
        for node in list_node:
            dict_path = nx.shortest_path_length(G, source=node, weight='weight')  # dict for return path length
            avg_path = round(sum(dict_path.values()) / len(dict_path), 3)  # precision until 3 decimal
            list_avgpath.append(avg_path)
            write_File_0.writerow([node, avg_path])

    tag_title = tag_PR + ': AVG Shortest Path Length Distribution'
    tag_x = 'Shortest Path Length * 10 times' #TODO it seems histogram having problem handling precision under 3 decimal
    tag_y = 'Portion of node Pk'
    fout_png = fout_png_name + '_hist' + '.png'

    my_plothist(list_avgpath, tag_title, tag_x, tag_y, fout_png)

    my_PrintOutFile(fout_csv)
    my_PrintTag(tag_PR, tag_ALGO)

