from src.myFunc import *


def my_maxclique(fin_gexf, fout_gexf):
    G = nx.read_gexf(fin_gexf)
    tag_PR = '2'
    tag_ALGO = 'max_clique'
    fout_txt = 'output/' + tag_PR + '_' + tag_ALGO + '.txt'

    cG = G.copy()
    set_clique_node = set()
    set_noncliqe_node = set(list(G.nodes))  # initialized with all nodes
    list_clique = list(nx.find_cliques(G))
    list_num = []  # the list to keep number of nodes in one clique
    for node in list_clique:
        list_num.append(len(node))
    max_num_clique = max(list_num)
    num_node = 0
    # adding all nodes in max clique to set
    with open(fout_txt, 'w') as f:
        f.write('gexf file: %s \n' % fin_gexf)
        for node in list_clique:
            if len(node) == max_num_clique:
                set_clique_node.update(node)
                num_node = num_node + 1
                f.write(str(node) + '\n')
        f.write('number of maximal clique: %d\n' % num_node)
        f.write('number node in maximal clique: %d\n' % max_num_clique)

    # remove nodes from list of all nodes, leaving non-clique node
    for node in set_clique_node:
        set_noncliqe_node.remove(node)
    # remove nodes from the graph
    cG.remove_nodes_from((list(set_noncliqe_node)))
    nx.write_gexf(cG, fout_gexf)
    my_PrintOutFile(fout_gexf)
    my_PrintOutFile(fout_txt)
    my_PrintTag(tag_PR, tag_ALGO)

    return cG
