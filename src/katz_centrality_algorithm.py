# Compute the Katz centrality for your network by setting alpha between and
# excluding 0.0 and 1/𝜆1. As for beta, set it first to 0.2, then to 0.5, and then
# to 1.

from src.myFunc import *


def my_katz(fin_gexf, fout_top10_csv_name, fout_gexf_name):

    tag_PR = '3b'
    tag_ALGO = 'Katz_centrality'

    attrG = nx.Graph()
    G = nx.read_gexf(fin_gexf)

    # use max(nx.adjacency_spectrum(G)) for eigen value calculation
    max_lambda = max(nx.adjacency_spectrum(G))
    max_alpha = 1/max_lambda.real
    list_alpha = []
    list_beta = [0.2, 0.5, 1.0]
    #list_beta = [0.1]
    list_dictkatz = []
    list_G = []

    for i in range(1, 10):
        list_alpha.append(i*(max_alpha/10))

    for beta in list_beta:
        fout_top10_csv = 'output/csv/' + tag_PR + '_Katz_alpha'+str(round(list_alpha[8], 3))+'_beta'+str(beta)+'_top10.csv'
        fout_gexf ='output/gexf/' + tag_PR + '_' + tag_ALGO + '_alpha'+str(round(list_alpha[8], 3))+'_beta'+str(beta)+'.gexf'

        # katz_centrality(G, alpha=0.1, beta=1.0, max_iter=1000, tol=1e-06)
        dict_katz = nx.katz_centrality(G, alpha=list_alpha[8], beta=beta, normalized=True, weight='weight')

        list_dictkatz.append(dict_katz)
        my_dictop2csv(dict_katz, fout_top10_csv, tag_ALGO)
        attrG = my_addattr2node(G, dict_katz, fout_gexf, tag_ALGO)
        list_G.append(attrG)
    fout_csv = 'output/csv/' + tag_PR + '_Katz_alpha' + str(round(list_alpha[8], 3)) + '_beta' + str(beta) + '.csv'
    my_dict2csv(dict_katz, fout_csv)
    my_PrintTag(tag_PR, tag_ALGO)
    return fout_gexf, dict_katz

