import csv
import networkx as nx

fTag = 'CREATE GRAPH'
input_ex_csv_name = 'data/example_out.csv'
output_ex_gexf_name = 'data/atp_match_graph.gexf'

input_csv_name = 'data/parse_match_scores_2017.csv'
out_path_MDG = 'data/MultiDiGraph_atp_match_2017.gexf'
out_path_MG = 'data/MultiGraph_atp_match_2017.gexf'
out_path_G = 'data/Graph_atp_match_2017.gexf'
out_path_sub_G = 'output/PR1_subGraph_atp_match_2017.gexf'

# create MultiDiGraph MDG
with open(input_csv_name, newline='') as inputFile:
    read_file = csv.reader(inputFile)
    #create MultiDiGraph, a directed graph with self loops and parallel edges.
    MDG = nx.MultiDiGraph(read_file)

MG = nx.MultiGraph(MDG)

# create Graph G and merge multiple match as weight
G = nx.Graph()
with open(input_csv_name, newline='') as inputFile:
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
nx.write_gexf(MDG, out_path_MDG)
nx.write_gexf(MG, out_path_MG)
nx.write_gexf(G, out_path_G)

# create subgraph with degree measurement
# TODO here degree is only counted as edge number, weight of edge is not considered
l_subNode = []
for node in list(G.nodes):
    if G.degree(node) > 10:
        l_subNode.append(node)
subG = G.subgraph(l_subNode)
nx.write_gexf(subG, out_path_sub_G)

#TODO making printing result a universal funtion for each module
print('========['+fTag+'] RESULT: SUCCESS========')
print('Output GEXF File Name: ' + out_path_MDG)