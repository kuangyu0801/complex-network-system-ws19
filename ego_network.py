import networkx as nx

f_input_gexf = 'data/Graph_atp_match_2017.gexf'
f_output_gexf = 'output/ego_network.gexf'

G = nx.read_gexf(f_input_gexf)
max_node = []
max_degree = 0
# Choose the node of max degree to be the most important node
for node in list(G.nodes):
    if G.degree(node) > max_degree:
        max_degree = G.degree(node)
        max_node = node
print('max_degree %d' % max_degree)
print('max_node %s' % max_node)

eG = nx.ego_graph(G, max_node)
nx.write_gexf(eG, f_output_gexf)