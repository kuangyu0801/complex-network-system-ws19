import csv
import networkx as nx

input_csv_name = 'data/example_out.csv'
output_gexf_name = 'data/atp_match_graph.gexf'
#G = nx.MultiDiGraph()
with open(input_csv_name, newline='') as inputFile:
    read_file = csv.reader(inputFile)

    #create MultiDiGraph, a directed graph with self loops and parallel edges.
    G = nx.MultiDiGraph(read_file)

print('Graph consist nodes: ', G.nodes)
print('Graph consist edges: ', G.edges)
nx.write_gexf(G, output_gexf_name)