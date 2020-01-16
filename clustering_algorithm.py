import csv
import networkx as nx
from myFunc import *

f_input_gexf = 'data/Graph_atp_match_2017.gexf'
f_output_dd_csv = 'output/csv/distance_distribution.csv'
f_output_cc_csv = 'output/csv/cc_distribution.csv'

tag_PR = '2'
tag_ALGO = 'degree_centrality'
tag_ALGO_1 = 'clustering_coeff'
fin_gexf = 'data/Graph_atp_match_2017.gexf'
fout_top10_csv = 'output/degree_top10.csv'
fout_gexf = 'output/gexf/' + tag_PR +'_'+  tag_ALGO + '.gexf'

dict_degree_cc = {}
dict_degree_avg = {}
G = nx.read_gexf(f_input_gexf)
list_degree = []
list_cc = []
with open(f_output_cc_csv, 'w', newline='') as outputFile_0:
    write_File_0 = csv.writer(outputFile_0)
    for node in list(G.nodes):
        degree = G.degree(node, weight='weight')
        list_degree.append(degree)
        cc = nx.clustering(G, nodes=node)
        list_cc.append(cc)

        if degree in dict_degree_cc.keys():
            list_tmp = dict_degree_cc[degree]
            # print(list_tmp)
            list_tmp.append(cc)
            # print(list_tmp)
            dict_degree_cc[degree] = list_tmp
        else:
            dict_degree_cc[degree] = [cc]

        write_File_0.writerow([node, degree, cc])


for degree in dict_degree_cc.keys():
    list_tmp = dict_degree_cc[degree]
    avg_cc = sum(list_tmp)/len(list_tmp)
    dict_degree_avg[degree] = avg_cc
    print('degree %s has average clustering of %f' % (degree, avg_cc))

tag_title = 'Degree vs. Average Clustering Coefficient'
tag_x = 'Degree'
tag_y = 'Average Clustering Coefficient'
list_key = list(dict_degree_avg.keys())
my_scatterplot(list(dict_degree_avg.keys()), list(dict_degree_avg.values()), tag_title, tag_x, tag_y)

#my_plothist(list_avgpath, tag_title, tag_x, tag_y)