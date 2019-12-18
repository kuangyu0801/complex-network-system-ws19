import csv
import networkx as nx

fTag = 'CREATE GRAPH'
input_ex_csv_name = 'data/example_out.csv'
output_ex_gexf_name = 'data/atp_match_graph.gexf'

input_csv_name = 'data/parse_match_scores_2017.csv'
output_gexf_name = 'data/atp_match_2017_graph.gexf'

#G = nx.MultiDiGraph()
with open(input_csv_name, newline='') as inputFile:
    read_file = csv.reader(inputFile)

    #create MultiDiGraph, a directed graph with self loops and parallel edges.
    G = nx.MultiDiGraph(read_file)

print('Graph consist nodes: ', G.nodes)
print('Graph consist edges: ', G.edges)
nx.write_gexf(G, output_gexf_name)

#TODO making printing result a universal funtion for each module
print('========['+fTag+'] RESULT: SUCCESS========')
print('Output GEXF File Name: ' + output_gexf_name)