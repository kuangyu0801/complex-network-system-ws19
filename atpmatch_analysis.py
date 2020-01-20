# Main python program: network_analysis.py
# TODO [PR0] making this the main program

from smallworld_algorithm import *
from clustering_algorithm import *

tag_PR = {2: 'PR2', 3: 'PR3a', 4: 'PR3b', 5: 'PR4a', 6: 'PR4b'}

# PR2

fin_gexf = 'data/Graph_atp_match_2017.gexf'
#f_output_dd_csv = 'output/csv/distance_distribution.csv'
#f_output_cc_csv = 'output/csv/cc_distribution.csv'
tag_PR = 'PR2'
tag_ALGO = 'degree_centrality'
#tag_ALGO_1 = 'clustering_coeff'
#fout_top10_csv = 'output/degree_top10.csv'
fout_gexf = 'output/gexf/' + tag_PR +'_'+  tag_ALGO + '.gexf'

#my_clustering(fin_gexf, tag_PR)


# PR3a

# PR3b

#TODO Try to merge all requirement from 3a to 3b into single csv

# PR4a

# PR4b

G = nx.read_gexf(fin_gexf)
k_link = round(my_avg_degree(G)/2)  # using only 1/2 of average degree
node_size = G.order()
p_prob = [0.001, 0.01, 0.1, 1]
for p in p_prob:
    my_smallworld(node_size, k_link, p)

tag_PR = 'PR4b'
tag_ALGO = 'Original'
tag_comb = tag_PR + '_' + tag_ALGO
fout_txt = 'output/' + tag_PR + '_' + tag_ALGO  + '.txt'

# calculating small-worldness with my own graph
my_calsmallworldness(G, fout_txt)
