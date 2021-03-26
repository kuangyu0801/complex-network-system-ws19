from src.myFunc import *


def my_degree_centrality(fin_gexf, fout_csv_name, fout_gexf_name):

    tag_PR = '3a'
    tag_ALGO = 'degree_centrality'
    fout_top10_csv = fout_csv_name + '_top10.csv'
    fout_gexf = 'output/gexf/' + tag_PR + '_' + tag_ALGO + '.gexf'
    fout_csv = fout_csv_name + '.csv'
    # TODO [PR2] check max degree centrality, not sure whether the degree centrality treats every edge as 1
    # For multigraphs or graphs with self loops the maximum degree might be higher than n-1
    # and values of degree centrality greater than 1 are possible.
    attrG = nx.Graph()
    G = nx.read_gexf(fin_gexf)
    dict_degree = nx.degree_centrality(G)
    my_dict2csv(dict_degree, fout_csv)
    my_dictop2csv(dict_degree, fout_top10_csv, tag_ALGO)
    attrG = my_addattr2node(G, dict_degree, fout_gexf, tag_ALGO)
    my_PrintTag(tag_PR, tag_ALGO)
    return fout_gexf, dict_degree
