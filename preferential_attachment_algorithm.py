from myFunc import *
from clustering_algorithm import *
from degree_distribution_algorithm import *

tag_PR = 'PR4b'
tag_ALGO = 'preferential_attachment'
fin_gexf = 'data/Graph_atp_match_2017.gexf'
f_txt_out = 'output/' + tag_PR + '_' + tag_ALGO + '.txt'

G = nx.read_gexf(fin_gexf)
m_link = round(my_avg_degree(G))
node_size = G.order()

baG = nx.barabasi_albert_graph(node_size, m_link, seed=None)

fout_gexf = 'output/gexf/' + tag_PR + '_' + tag_ALGO + '_n_' + str(node_size) + '_m_' + str(m_link) + '.gexf'

my_gexfwrite(baG, fout_gexf)

my_degreedist(fout_gexf, tag_PR + '_' + tag_ALGO)
my_clustering(fout_gexf, tag_PR + '_' + tag_ALGO)

# average path length
g_avg_path_len = nx.average_shortest_path_length(G)

with open(f_txt_out, 'w') as f:
    f.write('average path length: %f \n' % g_avg_path_len)
