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
with open(f_output_dd_csv, 'w', newline='') as outputFile_0, open(f_output_cc_csv, 'w', newline='') as outputFile_1:
    write_File_0 = csv.writer(outputFile_0)
    write_File_1 = csv.writer(outputFile_1)
    for node in list(G.nodes):
        degree = G.degree(node)
        dict_path = nx.shortest_path_length(G, source=node, weight='weight')  # dict for return path length
        avg_path = int(sum(dict_path.values())/len(dict_path))  # *100 times for distribution
        list_avgpath.append(avg_path)
        cc = nx.clustering(G, nodes=node)
        #avg_path = int(100 * sum(dict_path.values()) / len(dict_path))  # *100 times for distribution
        write_File_0.writerow([degree, avg_path])
        write_File_1.writerow([degree, cc])

tag_title = 'Average Shortest Path Length Distribution'
tag_x = 'Average Shortest Path Length'
tag_y = 'Distribution'
my_plothist(list_avgpath, tag_title, tag_x, tag_y)
