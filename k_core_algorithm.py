import networkx as nx
from myFunc import *


def my_kcore(fin_gexf, fout_nx_gexf_name, fout_my_gexf_name):

    G = nx.read_gexf(fin_gexf)
    kG = nx.k_core(G)
    max_degree = my_max_degree(G)
    cur_k = max_degree
    tmpG = G.copy()
    curG = nx.Graph()

    flag_first = False
    while (tmpG.order() < cur_k) or (flag_first == False): # algo stops when least order >= cur_k

        flag_first = True
        tmpG = G.copy()

        # Step 1- remove all nodes from the original graph that have a degree smaller than k
        # and all the incident nodes*
        # TODO could be simplified by using G.adj
        for i_node in list(G.nodes):
            #print(tmpG.degree(i_node))
            if (tmpG.has_node(i_node) == True) and (tmpG.degree(i_node) < cur_k):
                nbr_nodes = tmpG.neighbors(i_node)
                tmpG.remove_node(i_node)
                #print('remove node: ' + i_node)
                #TODO not sure about this part
                #tmpG.remove_nodes_from(nbr_nodes)
        # Step 2– remove nodes that have fewer than k neighbors
        for i_node in list(tmpG.nodes):
            if (tmpG.has_node(i_node) == True) and len(list((tmpG.neighbors(i_node)))) < cur_k:
                tmpG.remove_node(i_node)
            # Step 3– iterate until no remaining node has fewer than k neighbors
            for j_node in list(tmpG.nodes):
                if (tmpG.has_node(j_node) == True) and len(list((tmpG.neighbors(j_node)))) < cur_k:
                    tmpG.remove_node(j_node)
                    print('[iter_j]remove node %s with less %d neighbor ' % (j_node, cur_k))
                print('[iter_i]remove node %s with less %d neighbor ' % (i_node, cur_k))

        print('[cur_k: %d]' % cur_k)
        print('tmpG order: ' + str(tmpG.order()))
        print(list(tmpG.nodes))
        # Step 4– the remaining nodes form the k-core
        curG = tmpG
        cur_k = cur_k - 1
    final_k = (cur_k+1)
    print('final_k: %d' % int(cur_k+1))

    fout_my_gexf =  fout_nx_gexf_name + '_k_' + str(final_k) + '_my.gexf'
    fout_nx_gexf = fout_my_gexf_name + '_k_' + str(final_k) + '_nx.gexf'
    nx.write_gexf(kG, fout_nx_gexf)
    nx.write_gexf(curG, fout_my_gexf)

    my_PrintOutFile(fout_nx_gexf)
    my_PrintOutFile(fout_my_gexf)
    return fout_nx_gexf, fout_my_gexf
