import networkx as nx
from myFunc import *


def my_betweeness(fin_gexf, fout_top10_csv_name, fout_gexf_name):

    tag_PR = '3a'
    tag_ALGO = 'betweenness_centrality'
    fout_top10_csv = 'output/csv/' + tag_PR + '_' + tag_ALGO + '_top10.csv'
    fout_gexf = 'output/' + tag_PR + '_' + tag_ALGO + '.gexf'

    G = nx.read_gexf(fin_gexf)
    #  betweenness_centrality(G, k=None, normalized=True, weight=None, endpoints=False, seed=None)
    dict_between = nx.betweenness_centrality(G, normalized=True, weight='weight')
    my_dictop2csv(dict_between, fout_top10_csv, tag_ALGO)
    my_addattr2node(G, dict_between, fout_gexf, tag_ALGO)
    my_PrintTag(tag_PR, tag_ALGO)
    return fout_gexf