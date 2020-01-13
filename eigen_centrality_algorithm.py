# implementation of eigen centrality algorithm
import networkx as nx
from myFunc import *
tag_PR = '3a'
tag_ALGO = 'eigen_centrality'
fin_gexf = 'data/Graph_atp_match_2017.gexf'
fout_top10_csv = 'output/eigen_top10.csv'

G = nx.read_gexf(fin_gexf)

#  eigenvector_centrality(G, max_iter=100, tol=1e-06, nstart=None, weight=None)
dict_eigen = nx.eigenvector_centrality(G, max_iter=100,  tol=1e-06, weight='weight')

my_dictop2csv(dict_eigen, fout_top10_csv, tag_ALGO)
my_PrintTag(tag_PR, tag_ALGO)