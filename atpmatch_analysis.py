# Main python program: network_analysis.py
# TODO [PR0] making this the main program

from smallworld_algorithm import *
from clustering_algorithm import *
from max_clique_algorithm import *
from property_analyze import *
from egocentric_network_algorithm import *

#TODO making this a interactive on terminal so we won't always executing whole function
tag_PR = {2: '2', 3: '3a', 4: '3b', 5: '4a', 6: '4b'}
tag_ALGO = {1: 'property_analysis', 2: 'ego_network',10: 'degree_centrality'}
# PR1

# PR2

fin_gexf = 'data/Graph_atp_match_2017.gexf'

G = nx.read_gexf(fin_gexf)

if False:
    ftxt_out = 'output/' + tag_PR[2] + '_' + tag_ALGO[1] + '.txt'
    my_property(G, ftxt_out)


fout_gexf = 'output/gexf/' + tag_PR[2] + '_' + tag_ALGO[2] + '.gexf'
#TODO making this a automatic function
most_node = 'DAVID-GOFFIN' # #1 node in page rank
eG = my_egonetwork(G, most_node)

ftxt_out = 'output/' + tag_PR[2] + '_' + tag_ALGO[2] + '.txt'
print(ftxt_out)
my_property(eG, ftxt_out)
if False:
    maxclique_G = my_maxclique(G)
    my_clustering(fin_gexf, tag_PR)


# PR3a

# PR3b

#TODO Try to merge all requirement from 3a to 3b into single csv

# PR4a

# PR4b
if False:
    G = nx.read_gexf(fin_gexf)
    k_link = round(my_avg_degree(G)/2)  # using only 1/2 of average degree
    node_size = G.order()
    p_prob = [0.001, 0.01, 0.1, 1]
    for p in p_prob:
        my_smallworld(node_size, k_link, p)

    tag_PR = 'PR4b'
    tag_ALGO = 'Original'
    tag_comb = tag_PR + '_' + tag_ALGO
    fout_txt = 'output/' + tag_PR + '_' + tag_ALGO + '.txt'

    # calculating small-worldness with my own graph
    my_calsmallworldness(G, fout_txt)
