import networkx as nx
from myFunc import *
tag_PR = '3a'
tag_ALGO = 'degree centrality'
fin_gexf = 'data/Graph_atp_match_2017.gexf'
fout_top10_csv = 'output/degree_top10.csv'

G = nx.read_gexf(fin_gexf)
dict_degree = nx.degree_centrality(G)
my_dictop2csv(dict_degree, fout_top10_csv, tag_ALGO)
my_PrintTag(tag_PR, tag_ALGO)