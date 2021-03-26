# implementation of eigen centrality algorithm
from src.myFunc import *


def my_eigen(fin_gexf, fout_csv_name, fout_gexf_name):

    tag_PR = '3a'
    tag_ALGO = 'eigen_centrality'
    fout_top10_csv = 'output/csv/' + tag_PR + '_' + tag_ALGO + '_top10.csv'
    fout_gexf = 'output/gexf/' + tag_PR + '_' + tag_ALGO + '.gexf'
    fout_csv = fout_csv_name + '.csv'

    G = nx.read_gexf(fin_gexf)

    #  eigenvector_centrality(G, max_iter=100, tol=1e-06, nstart=None, weight=None)
    dict_eigen = nx.eigenvector_centrality(G, max_iter=100,  tol=1e-06, weight='weight')

    my_dict2csv(dict_eigen, fout_csv)
    my_dictop2csv(dict_eigen, fout_top10_csv, tag_ALGO)
    my_addattr2node(G, dict_eigen, fout_gexf, tag_ALGO)
    my_PrintTag(tag_PR, tag_ALGO)
    return fout_gexf, dict_eigen
