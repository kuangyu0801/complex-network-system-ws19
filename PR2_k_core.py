import networkx as nx
from myFunc import *

f_input_gexf = 'data/Graph_atp_match_2017.gexf'
f_output_nx_kcore = 'output/nx_k_core.gexf'
f_output_my_kcore = 'output/my_k_core.gexf'


if True:
    G = nx.read_gexf(f_input_gexf)
else:
    G = nx.complete_graph(9)
kG = nx.k_core(G)
max_degree = my_max_degree(G)
#for i in range(max_degree):

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

print('final_k: %d' % int(cur_k+1))
my_min_degree(curG)  # check
my_min_degree(kG)  # check
nx.write_gexf(kG, f_output_nx_kcore)
nx.write_gexf(curG, f_output_my_kcore)