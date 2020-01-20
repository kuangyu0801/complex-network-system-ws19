from myFunc import *
from clustering_algorithm import *
from degree_distribution_algorithm import *


def my_smallworld(node_size, k_link, p_prob):
    tag_PR = 'PR4b'
    tag_ALGO = 'smallworld'
    tag_comb = tag_PR + '_' + tag_ALGO + '_n_' + str(node_size) + '_k_' + str(k_link) + '_p_' + str(p_prob)
    fout_gexf = 'output/gexf/' + tag_comb + '.gexf'
    fout_txt = 'output/' + tag_comb + '.txt'

    # watts_strogatz_graph
    wsG = nx.watts_strogatz_graph(node_size, k_link, p_prob, seed=None)

    my_gexfwrite(wsG, fout_gexf)

    my_degreedist(fout_gexf, tag_comb)
    my_clustering(fout_gexf, tag_comb)
    my_calsmallworldness(wsG, fout_txt)

    return wsG


def my_calsmallworldness(G, fout_txt):

    g_avg_path_len = nx.average_shortest_path_length(G)
    g_avg_cluster_coeff = nx.average_clustering(G)
    g_smallworld = g_avg_cluster_coeff/g_avg_path_len
    with open(fout_txt, 'w') as f:
        f.write('clustering coefficient: %f \n' % g_avg_cluster_coeff)
        f.write('average path length: %f \n' % g_avg_path_len)
        f.write('Small-Worldness: %f \n' % g_smallworld)

    return g_smallworld
