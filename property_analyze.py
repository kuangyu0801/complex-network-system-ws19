import networkx as nx

# reading from a undirected graph
f_input_gexf = 'data/Graph_atp_match_2017.gexf'
f_txt_out = 'data/property.txt'
#TODO: find out about degree, diameter, subgraph
# for simplicity, I computed the graph with undirected graph

G = nx.read_gexf(f_input_gexf)

# order
g_order = G.order()

# size
g_size = G.size()

# density
g_dens = nx.density(G)

# diameter
g_diameter = nx.diameter(G)

# radius
g_radius = nx.radius(G)

# average path length
g_avg_path_len = nx.average_shortest_path_length(G)

# average clustering coefficient
d_cluster = nx.clustering(G) # return a floating dictionary
sum_cluster = 0
for value in d_cluster.values():
    sum_cluster = sum_cluster + value

len(d_cluster)
g_avg_cluster_coeff_hand = sum_cluster/g_order
g_avg_cluster_coeff = nx.average_clustering(G)

# transitivity
# TODO disable transitivity for not implemented for multigraph type
g_trans = nx.transitivity(G)

# number of triangle
d_trian = nx.triangles(G)  # returning a dictionary
sum_tri = 0
for value in d_cluster.values():
    sum_tri = sum_tri + value
g_num_trian = sum_tri

# number of clique
l_clique = list(nx.find_cliques(G))
g_num_clique = len(l_clique)

# connected component
g_num_conn = nx.number_connected_components(G)

with open(f_txt_out, 'w') as f:
    f.write('order: %d \n' % g_order)
    f.write('size: %d \n' % g_size)
    f.write('density: %d \n' % g_dens)
    f.write('diameter:%d \n' % g_diameter)
    f.write('radius: %d \n' % g_radius)
    f.write('average path length: %f \n' % g_avg_path_len)
    f.write('transitivity: %f \n' % g_trans)
    f.write('number of triangle: %d \n' % g_num_trian)
    f.write('number of clique: %d \n' % g_num_clique)
    f.write('number of component: %d \n' % g_num_conn)
