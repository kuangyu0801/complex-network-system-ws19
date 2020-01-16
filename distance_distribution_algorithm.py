import csv
import networkx as nx
from myFunc import *

f_input_gexf = 'data/Graph_atp_match_2017.gexf'
f_output_dd_csv = 'output/csv/distance_distribution.csv'
f_output_cc_csv = 'output/csv/cc_distribution.csv'

tag_PR = '2'
tag_ALGO = 'degree_centrality'
tag_ALGO_1 = 'clustering_coeff'
fin_gexf = 'data/Graph_atp_match_2017.gexf'
fout_top10_csv = 'output/degree_top10.csv'
fout_gexf = 'output/gexf/' + tag_PR +'_'+  tag_ALGO + '.gexf'


G = nx.read_gexf(f_input_gexf)
list_avgpath = []
list_node = list(G.nodes())
first_node = list_node[1]
#  print(list_node[1])

# degree = G.degree(node)
dict_path = nx.shortest_path_length(G, source=first_node, weight='weight')  # dict for return path length
avg_path = round(sum(dict_path.values()) / len(dict_path), 3)  #
list_avgpath = list(dict_path.values())

with open(f_output_dd_csv, 'w', newline='') as outputFile_0:
    write_File_0 = csv.writer(outputFile_0)
    #TODO print starting node and average path length
    #TODO change to 折線圖
    #TODO fix distribution sum > 1
    for node in dict_path.keys():
        write_File_0.writerow([node, dict_path[node]])

tag_title = 'Shortest Path Length Distribution'
tag_x = 'Shortest Path Length'
tag_y = 'Distribution'


my_plothist(list_avgpath, tag_title, tag_x, tag_y)