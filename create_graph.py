import csv
import networkx as nx

fTag = 'CREATE GRAPH'
input_ex_csv_name = 'data/example_out.csv'
output_ex_gexf_name = 'data/atp_match_graph.gexf'

input_csv_name = 'data/parse_match_scores_2017.csv'
output_gexf_name = 'data/atp_match_2017_graph.gexf'
output_path_MultiGraph = 'data/MultiGraph_atp_match_2017.gexf'
output_path_Graph = 'data/Graph_atp_match_2017.gexf'

#G = nx.MultiDiGraph()
with open(input_csv_name, newline='') as inputFile:
    read_file = csv.reader(inputFile)
    #create MultiDiGraph, a directed graph with self loops and parallel edges.
    G = nx.MultiDiGraph(read_file)

G_multi = nx.MultiGraph(G)
G_simple = nx.Graph(G)

print('Graph consist nodes: ', G.nodes)
print('Graph consist edges: ', G.edges)
nx.write_gexf(G, output_gexf_name)
nx.write_gexf(G_multi, output_path_MultiGraph)
nx.write_gexf(G_simple, output_path_Graph)

#TODO making printing result a universal funtion for each module
print('========['+fTag+'] RESULT: SUCCESS========')
print('Output GEXF File Name: ' + output_gexf_name)