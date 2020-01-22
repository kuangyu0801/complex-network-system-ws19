# Main python program: network_analysis.py
# TODO [PR0] making this the main program

from smallworld_algorithm import *
from clustering_algorithm import *
from max_clique_algorithm import *
from property_analyze import *
from egocentric_network_algorithm import *
from distance_distribution_algorithm import *
from k_core_algorithm import *

#TODO making this a interactive on terminal so we won't always executing whole function
tag_PR = {2: '2', 3: '3a', 4: '3b', 5: '4a', 6: '4b'}
tag_ALGO = {2: {1: 'property_analysis', 2: 'ego_network', 3: 'distance_distribution',
                5: 'clustering_coeff', 4: 'max_clique', 6: 'k_core'},
            10: 'degree_centrality'}

# PR1

# PR2

fin_gexf = 'data/Graph_atp_match_2017.gexf'
fout_ego_name = 'output/gexf/' + tag_PR[2] + '_' + tag_ALGO[2][2]

G = nx.read_gexf(fin_gexf)

# property_analysis for original network
if False:
    ftxt_out = 'output/' + tag_PR[2] + '_' + tag_ALGO[2][1] + '.txt'

    my_property(fin_gexf, ftxt_out)

# distance_distribution for original network
if False:
    fout_png_name = 'output/pic/' + tag_PR[2] + '_' + tag_ALGO[2][3]
    fout_csv = 'output/csv/' + tag_PR[2] + '_' + tag_ALGO[2][3] + '.csv'

    my_distance_dist(fin_gexf, fout_csv,  fout_png_name)

# ego_network
if False:
    #TODO make the first node selectable from pagerank...
    most_node = 'DAVID-GOFFIN' # #1 node in page rank
    ftxt_out = 'output/' + tag_PR[2] + '_' + tag_ALGO[2][2] + '.txt'

    fout_ego_gexf, eG = my_egonetwork(G, fout_ego_name, most_node)
    my_property(fout_ego_gexf, ftxt_out) # property_analysis for ego

# clustering vs degree
if False:
    my_clustering(fin_gexf, tag_PR[2])

# k_core
if False:
    fout_my_gexf_name = 'output/gexf/' + tag_PR[2] + '_' + tag_ALGO[2][6]
    fout_nx_gexf_name = 'output/gexf/' + tag_PR[2] + '_' + tag_ALGO[2][6]
    fout_nx_gexf, fout_my_gexf = my_kcore(fin_gexf, fout_my_gexf_name, fout_nx_gexf_name)

    fout_my_txt = 'output/' + tag_PR[2] + '_' + tag_ALGO[2][6] + '_my.txt'
    fout_nx_txt = 'output/' + tag_PR[2] + '_' + tag_ALGO[2][6] + '_nx.txt'
    my_property(fout_my_gexf, fout_my_txt)  # property_analysis for ego
    my_property(fout_nx_gexf, fout_nx_txt)  # property_analysis for ego


# max_clique
if False:
    fout_max_clique_gexf = 'output/gexf/' + tag_PR[2] + '_' + tag_ALGO[2][4] + '.gexf'
    maxclique_G = my_maxclique(fin_gexf, fout_max_clique_gexf)

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
