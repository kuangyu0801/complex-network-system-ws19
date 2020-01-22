import networkx as nx
from myFunc import *
from clustering_algorithm import *
from degree_distribution_algorithm import *
def my_randomgraph(fin_gexf, fout_gexf_name):
    tag_PR = '4a'
    list_degree = list()

    G = nx.read_gexf(fin_gexf)

    for node in list(G.nodes()):
        list_degree.append(nx.degree(G, node, weight='weight'))

    node_size = G.order()
    avg_degree = sum(list_degree)/node_size
    prob = avg_degree/(node_size - 1)

    #  gnp_random_graph(n, p, seed=None, directed=False)
    rG = nx.gnp_random_graph(node_size, prob, seed=None, directed=False)

    fout_gexf = fout_gexf_name + '_n_' + str(node_size) + '_k_' + str(round(avg_degree,3)) + '_prob_' + str(round(prob, 3)) + '.gexf'
    nx.write_gexf(rG, fout_gexf)

    # output clustering distribution
    my_clustering(fout_gexf, tag_PR)

    # print degree distribution
    my_degreedist(fout_gexf, tag_PR)

    my_PrintOutFile(fout_gexf)
    my_PrintTag(tag_PR, 'random_graph')
    return fout_gexf
