from src.myFunc import *


def my_egonetwork(G, fout_gexf, most_node):

    tag_PR = '2'
    tag_ALGO = 'ego_network'
    fout_gexf = fout_gexf + '_' + most_node + '.gexf'
    eG = nx.ego_graph(G, most_node)
    nx.write_gexf(eG, fout_gexf)

    my_PrintOutFile(fout_gexf)
    my_PrintTag(tag_PR, tag_ALGO)
    return fout_gexf, eG
