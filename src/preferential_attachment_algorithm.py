import math

from src.clustering_algorithm import *
from src.degree_distribution_algorithm import *


def my_preferattach(fin_gexf):
    tag_PR = '4b'
    tag_ALGO = 'preferential_attachment'

    G = nx.read_gexf(fin_gexf)
    m_link = round(my_avg_degree(G)/2)
    node_size = G.order()
    fout_gexf = 'output/gexf/' + tag_PR + '_' + tag_ALGO + '_n_' + str(node_size) + '_m_' + str(m_link) + '.gexf'
    ftxt_out = 'output/' + tag_PR + '_' + tag_ALGO + '_n_' + str(node_size) + '_m_' + str(m_link) + '.txt'

    baG = nx.barabasi_albert_graph(node_size, m_link, seed=None)

    my_gexfwrite(baG, fout_gexf)
    my_degreedist(fout_gexf, tag_PR + '_' + tag_ALGO)
    my_clustering(fout_gexf, tag_PR + '_' + tag_ALGO)

    # average path length
    g_avg_path_len = nx.average_shortest_path_length(G)

    with open(ftxt_out, 'w') as f:
        f.write('gexf file: %s \n' % fin_gexf)
        f.write('average path length: %f \n' % g_avg_path_len)
    my_PrintOutFile(ftxt_out)
    my_PrintTag(tag_PR, tag_ALGO)
    return fout_gexf


def my_scalefree(fin_gexf):
    G = nx.read_gexf(fin_gexf)
    max_de = my_max_degree(G)
    min_de = my_min_degree(G)
    node_num = G.order()
    alpha = (math.log(node_num)/(math.log(max_de/min_de))) + 1
    return alpha
