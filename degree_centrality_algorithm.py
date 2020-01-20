import networkx as nx
from myFunc import *
tag_PR = '3a'
tag_ALGO = 'degree_centrality'
fin_gexf = 'data/Graph_atp_match_2017.gexf'
fout_top10_csv = 'output/csv/' + tag_PR + '_' + tag_ALGO + '_top10.csv'
fout_gexf = 'output/gexf/' + tag_PR + '_' + tag_ALGO + '.gexf'

# TODO [PR2] check max degree centrality, not sure whether the degree centrality treats every edge as 1
# For multigraphs or graphs with self loops the maximum degree might be higher than n-1
# and values of degree centrality greater than 1 are possible.
attrG = nx.Graph()
G = nx.read_gexf(fin_gexf)
dict_degree = nx.degree_centrality(G)
my_dictop2csv(dict_degree, fout_top10_csv, tag_ALGO)
attrG = my_addattr2node(G, dict_degree, fout_gexf, tag_ALGO)
my_PrintTag(tag_PR, tag_ALGO)