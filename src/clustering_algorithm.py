from src.myFunc import *


def my_clustering(fin_gexf, tag_PR):

    fout_csv = 'output/csv/' + tag_PR + '_clustering_coeff.csv'
    fout_png = 'output/pic/' + tag_PR + '_clustering_coeff.png'
    dict_degree_cc = {}
    dict_degree_avg = {}
    G = nx.read_gexf(fin_gexf)
    list_degree = []
    list_cc = []
    with open(fout_csv, 'w', newline='') as outputFile_0:
        write_File_0 = csv.writer(outputFile_0)
        for node in list(G.nodes):
            degree = G.degree(node, weight='weight')
            list_degree.append(degree)
            cc = nx.clustering(G, nodes=node)
            list_cc.append(cc)

            if degree in dict_degree_cc.keys():
                list_tmp = dict_degree_cc[degree]
                list_tmp.append(cc)
                dict_degree_cc[degree] = list_tmp
            else:
                dict_degree_cc[degree] = [cc]

            write_File_0.writerow([node, degree, cc])

    for degree in dict_degree_cc.keys():
        list_tmp = dict_degree_cc[degree]
        avg_cc = sum(list_tmp)/len(list_tmp)
        dict_degree_avg[degree] = avg_cc

    tag_title = tag_PR + ': Degree vs. Clustering Coefficient' + '\n' + fin_gexf
    tag_x = 'Degree k'
    tag_y = 'Clustering Coefficient'

    # TODO consider showing – nx.average_clustering(g)
    my_scatterplot(list(dict_degree_avg.keys()), list(dict_degree_avg.values()), tag_title, tag_x, tag_y, fout_png, False)
    fout_png = 'output/pic/' + tag_PR + '_clustering_coeff' + '_log' + '.png'
    my_scatterplot(list(dict_degree_avg.keys()), list(dict_degree_avg.values()), tag_title, tag_x, tag_y, fout_png, True)


#my_plothist(list_avgpath, tag_title, tag_x, tag_y)