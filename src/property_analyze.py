from src.myFunc import *
# reading from a undirected graph


def my_property(fin_gexf, ftxt_out):
    tag_PR = '2'
    tag_ALGO = 'property_analysis'
    # for simplicity, I computed the graph with undirected graph
    G = nx.read_gexf(fin_gexf)
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
    g_avg_cluster_coeff = nx.average_clustering(G, weight='weight')

    # transitivity
    g_trans = nx.transitivity(G)

    # number of triangle
    dict_trian = nx.triangles(G)  # returning a dictionary
    g_num_trian = sum(list(dict_trian.values()))/3  # a triangle is counted 3 times (1 for each node)

    # number of clique
    l_clique = list(nx.find_cliques(G))
    g_num_clique = len(l_clique)

    # connected component
    g_num_conn = nx.number_connected_components(G)

    with open(ftxt_out, 'w') as f:
        f.write('gexf file: %s \n' % fin_gexf)
        f.write('order: %d \n' % g_order)
        f.write('size: %d \n' % g_size)
        f.write('density: %f \n' % g_dens)
        f.write('diameter:%d \n' % g_diameter)
        f.write('radius: %d \n' % g_radius)
        f.write('average path length: %f \n' % g_avg_path_len)
        f.write('average clustering coefficient: %f \n' % g_avg_cluster_coeff)
        f.write('transitivity: %f \n' % g_trans)
        f.write('number of triangle: %d \n' % g_num_trian)
        f.write('number of clique: %d \n' % g_num_clique)
        f.write('number of component: %d \n' % g_num_conn)
    my_PrintOutFile(ftxt_out)
    my_PrintTag(tag_PR, tag_ALGO)
