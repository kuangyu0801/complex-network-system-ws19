#TODO [PR2] finish this part

# Find and list all maximal cliques

from myFunc import *


tag_PR = '2'
tag_ALGO = 'max_clique'
fin_gexf = 'data/Graph_atp_match_2017.gexf'
fout_csv = 'output/csv/' + tag_PR + '_' + tag_ALGO + '.csv'
fout_gexf = 'output/gexf/' + tag_PR + '_' + tag_ALGO + '.gexf'
list_clique = []
G = nx.read_gexf(fin_gexf)
list_clique = list(nx.find_cliques(G))

# remove nodes that are not in the list
print(list_clique)
