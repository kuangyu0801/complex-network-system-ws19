# Compute the Katz centrality for your network by setting alpha between and
# excluding 0.0 and 1/𝜆1. As for beta, set it first to 0.2, then to 0.5, and then
# to 1.

import networkx as nx
from myFunc import *
import numpy


tag_PR = '3b'
tag_ALGO = 'Katz_centrality'
fin_gexf = 'data/Graph_atp_match_2017.gexf'
fout_top10_csv = 'output/csv/' + tag_PR + '_' + tag_ALGO + '_top10.csv'
fout_gexf = 'output/' + tag_PR + '_' + tag_ALGO + '.gexf'


attrG = nx.Graph()
G = nx.read_gexf(fin_gexf)
# use max(nx.adjacency_spectrum(G)) for eigen value calculation
max_lambda = max(nx.adjacency_spectrum(G))
max_alpha = 1/max_lambda.real
list_alpha = []
list_beta = [0.2, 0.5, 1.0]
list_dictkatz = []
list_G = []
for i in range(1, 10):
    list_alpha.append(i*(max_alpha/10))

# katz_centrality(G, alpha=0.1, beta=1.0, max_iter=1000, tol=1e-06,
# nstart=None, normalized=True, weight=None)
for beta in list_beta:
    fout_top10_csv = 'output/csv/' + tag_PR + '_Katz_top10_alpha'+str(round(list_alpha[8], 3))+'_beta'+str(beta)+'.csv'
    fout_gexf ='output/gexf/' + tag_PR + '_' + tag_ALGO + '_alpha'+str(round(list_alpha[8], 3))+'_beta'+str(beta)+'.gexf'

    dict_katz = nx.katz_centrality(G, alpha=list_alpha[8], beta=beta, normalized=True, weight='weight')
    list_dictkatz.append(dict_katz)

    my_dictop2csv(dict_katz, fout_top10_csv, tag_ALGO)

    attrG = my_addattr2node(G, dict_katz, fout_gexf, tag_ALGO)
    list_G.append(attrG)

my_PrintTag(tag_PR, tag_ALGO)
