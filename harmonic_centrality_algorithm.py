#  implementation of harmonic centrality algorithm
import networkx as nx
import csv
from myFunc import *

tag_PR = '3a'
tag_ALGO = 'harmonic centrality'
fin_gexf = 'data/Graph_atp_match_2017.gexf'
fout_top10_csv = 'output/harmonic_top10.csv'

dict_name = {}
dict_order = {}
G = nx.read_gexf(fin_gexf)
dict_harmo = nx.harmonic_centrality(G, nbunch=None, distance='weight')
n_idx = 0
for node in dict_harmo.keys():
    n_idx = n_idx + 1
    dict_order[n_idx] = dict_harmo[node]
    dict_name[n_idx] = node

# print(dict_harmo)
# return a list of tuple (name_index, harmonic value)
list_harmo_sorted = sorted(dict_order.items(), key=lambda kv: (kv[1], kv[0]), reverse = True)
# print(list_harmo_sorted)

with open(fout_top10_csv, 'w', newline='') as outputFile:

    write_File = csv.writer(outputFile)
    for i in range(0, 9):
        x = list_harmo_sorted.pop(i)
        print(x)
        node = dict_name[x[0]]
        value = dict_harmo[node]
        write_File.writerow([node, value])
        print('%s has harmonic %f :' % (node, value))
        if value != x[1]:
            print('dictionary lookup error')
    if False:
        for node in dict_harmo_sorted.keys():
            count = count+1
            value = round(dict_harmo_sorted[node], 3)
            print('%s has harmonic %f :' % (node, value))
            write_File.writerow([node, value])
            if count == 9:
                break

my_PrintFile(fin_gexf, fout_top10_csv)
my_PrintTag(tag_PR, tag_ALGO)