import csv
import networkx as nx
from myFunc import *

fTag = 'CREATE GRAPH'

input_csv_name = ['data/parse_match_scores_1996-2016.csv', 'data/parse_match_scores_1991-2016.csv', 'data/parse_match_scores_2017.csv']
out_path_MDG = ['data/MultiDiGraph_atp_match_1991-2016.gexf', 'data/MultiDiGraph_atp_match_2017.gexf']
out_path_MG = ['data/MultiGraph_atp_match_1991-2016.gexf', 'data/MultiGraph_atp_match_2017.gexf']
out_path_G = ['data/Graph_atp_match_1996-2016.gexf', 'data/Graph_atp_match_1991-2016.gexf', 'data/Graph_atp_match_2017.gexf']
out_path_sub_G = ['data/Graph_subGraph_atp_match_1996-2016.gexf', 'data/Graph_subGraph_atp_match_1991-2016.gexf', 'output/PR1_subGraph_atp_match_2017.gexf']

input_csv = input_csv_name[0]
output_gexf = [out_path_G[0], out_path_sub_G[0]]
# create Graph G and merge multiple match as weight
G = nx.Graph()
with open(input_csv, newline='') as inputFile:
    read_file = csv.reader(inputFile)
    iter_rows = iter(read_file)
    for row in iter_rows:
        print(row)
        if G.has_edge(row[0], row[1]):
            curW = G[row[0]][row[1]]['weight']
            G[row[0]][row[1]]['weight'] = curW + 1
        else:
            G.add_edge(row[0], row[1], weight=1)

print('Graph consist nodes: ', G.nodes)
print('Graph consist edges: ', G.edges)
nx.write_gexf(G, output_gexf[0])
my_PrintOutFile(output_gexf[0])

# create subgraph with degree measurement
# TODO here degree is only counted as edge number, weight of edge is not considered
l_subNode = []
for node in list(G.nodes):
    if G.degree(node, weight='weight') > 10:
        l_subNode.append(node)
subG = G.subgraph(l_subNode)
nx.write_gexf(subG, output_gexf[1])
my_PrintOutFile(output_gexf[1])

#TODO [optional] making printing result a universal funtion for each module
print('========['+fTag+'] RESULT: SUCCESS========')