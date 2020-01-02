import networkx as nx

f_input_gexf = 'data/MultiGraph_atp_match_2017.gexf'
G = nx.read_gexf(f_input_gexf)
# number of clique
l_clique = list(nx.find_cliques(G))
g_num_clique = len(l_clique)
f_txt_out = 'data/property.txt'
s = 10
with open(f_txt_out, 'w') as f:
    f.write('Hello, world! %d\n' % s)
    f.write('Hello, world!!!')

