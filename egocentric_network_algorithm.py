from myFunc import *

def my_egonetwork(G, fout_gexf):

    tag_PR = '2'
    tag_ALGO = 'ego_network'
    max_node = []
    max_degree = 0
    # TODO [PR2] making most important node a choice of import
    # Choose the node of max degree to be the most important node
    for node in list(G.nodes):
        if G.degree(node) > max_degree:
            max_degree = G.degree(node)
            max_node = node
    print('max_degree %d' % max_degree)
    print('max_node %s' % max_node)
    eG = nx.ego_graph(G, max_node)
    nx.write_gexf(eG, fout_gexf)

    my_PrintOutFile(fout_gexf)
    my_PrintOutFile(fout_txt)
    my_PrintTag(tag_PR, tag_ALGO)
    return eG
