# Compute the PageRank for all nodes of your network

import networkx as nx
from myFunc import *
import numpy


tag_PR = '3b'
tag_ALGO = 'pagerank'
fin_gexf = 'data/Graph_atp_match_2017.gexf'
fout_top10_csv = 'output/csv/' + tag_PR + '_' + tag_ALGO + 'top10.csv'
fout_gexf = 'output/gexf/' + tag_PR + '_' + tag_ALGO + '.gexf'

list_alpha = []
max_range = 20
#making a choice of alph between 0.05 to 1
for i in range(0, max_range):
    list_alpha.append( round( (i+1) * (1/max_range), 2))

attrG = nx.Graph()
G = nx.read_gexf(fin_gexf)

#  pagerank(G, alpha=0.85, personalization=None, max_iter=100, tol=1e-06, nstart=None, weight='weight', dangling=None)

dict_pagerank = nx.pagerank(G, alpha=list_alpha[16], weight='weight')
my_dictop2csv(dict_pagerank, fout_top10_csv, tag_ALGO)
attrG = my_addattr2node(G, dict_pagerank, fout_gexf, tag_ALGO)

