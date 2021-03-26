# Compute the PageRank for all nodes of your network

from src.myFunc import *


def my_pagerank(fin_gexf, fout_top10_csv_name, fout_gexf_name):

    tag_PR = '3b'
    tag_ALGO = 'pagerank'
    list_alpha = []
    max_range = 20
    #making a choice of alph between 0.05 to 1
    for i in range(0, max_range):
        list_alpha.append(round((i+1) * (1/max_range), 2))

    G = nx.read_gexf(fin_gexf)
    #  pagerank(G, alpha=0.85, personalization=None, max_iter=100, tol=1e-06, nstart=None, weight='weight', dangling=None)
    dict_pagerank = nx.pagerank(G, alpha=list_alpha[16], weight='weight') # alpha is chosen to be 0.85

    fout_top10_csv = fout_top10_csv_name + '_alpha_' + str(list_alpha[16]) + '_top10.csv'
    fout_csv = fout_top10_csv_name + '_alpha_' + str(list_alpha[16]) + '.csv'
    my_dict2csv(dict_pagerank, fout_csv)
    my_dictop2csv(dict_pagerank, fout_top10_csv, tag_ALGO)

    fout_gexf = fout_gexf_name + '_alpha_' + str(list_alpha[16]) + '.gexf'
    attrG = my_addattr2node(G, dict_pagerank, fout_gexf, tag_ALGO)
    return fout_gexf, dict_pagerank

