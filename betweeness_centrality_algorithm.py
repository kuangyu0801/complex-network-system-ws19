import networkx as nx
from myFunc import *
tag_PR = '3a'
tag_ALGO = 'betweenness centrality'
fin_gexf = 'data/Graph_atp_match_2017.gexf'
fout_top10_csv = 'output/betweenness_top10.csv'

G = nx.read_gexf(fin_gexf)
#  betweenness_centrality(G, k=None, normalized=True, weight=None, endpoints=False, seed=None)
dict_between = nx.betweenness_centrality(G, normalized=True, weight='weight')
my_dictop2csv(dict_between, fout_top10_csv, tag_ALGO)
my_PrintTag(tag_PR, tag_ALGO)