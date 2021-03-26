#  implementation of harmonic centrality algorithm
from src.myFunc import *


def my_harmonic(fin_gexf, fout_csv_name, fout_gexf_name):

    tag_PR = '3a'
    tag_ALGO = 'harmonic_centrality'
    fout_top10_csv = 'output/csv/' + tag_PR + '_' + tag_ALGO + '_top10.csv'
    fout_gexf = 'output/gexf/' + tag_PR + '_' + tag_ALGO + '.gexf'
    fout_csv = fout_csv_name + '.csv'
    dict_name = {}
    dict_order = {}
    G = nx.read_gexf(fin_gexf)
    node_size = G.order()

    # harmonic_centrality is defined as sum(1/shortes_path) so we need adjust
    dict_harmo = nx.harmonic_centrality(G, nbunch=None, distance='weight')
    n_idx = 0
    for node in dict_harmo.keys():
        dict_harmo[node] = dict_harmo[node]/(node_size - 1)  # normalized for equation
        n_idx = n_idx + 1
        dict_order[n_idx] = dict_harmo[node]
        dict_name[n_idx] = node

    # return a sorted list of tuple (name_index, harmonic value)
    list_harmo_sorted = sorted(dict_order.items(), key=lambda kv: (kv[1], kv[0]), reverse = True)
    my_dict2csv(dict_harmo, fout_csv)
    my_dictop2csv(dict_harmo, fout_top10_csv, tag_ALGO)
    my_addattr2node(G, dict_harmo, fout_gexf, tag_ALGO)
    my_PrintTag(tag_PR, tag_ALGO)
    return fout_gexf, dict_harmo
