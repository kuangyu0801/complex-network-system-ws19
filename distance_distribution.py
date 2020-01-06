import csv
import networkx as nx

f_input_gexf = 'data/Graph_atp_match_2017.gexf'
f_output_dd_csv = 'output/distance_distribution.csv'
f_output_cc_csv = 'output/cc_distribution.csv'

G = nx.read_gexf(f_input_gexf)
with open(f_output_dd_csv, 'w', newline='') as outputFile_0, open(f_output_cc_csv, 'w', newline='') as outputFile_1:
    write_File_0 = csv.writer(outputFile_0)
    write_File_1 = csv.writer(outputFile_1)
    for node in list(G.nodes):
        degree = G.degree(node)
        dict_path = nx.shortest_path_length(G, source=node) # dict for return path length
        avg_path = int(100*sum(dict_path.values())/len(dict_path)) # *100 times for distribution
        cc = nx.clustering(G, nodes=node)
        #avg_path = int(100 * sum(dict_path.values()) / len(dict_path))  # *100 times for distribution
        write_File_0.writerow([degree, avg_path])
        write_File_1.writerow([degree, cc])
