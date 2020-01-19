import networkx as nx
import csv
import numpy as np
import matplotlib.pyplot as plt


def my_gexfwrite(G, fout_gexf):
    nx.write_gexf(G, fout_gexf)
    print('[WRITE_GEXF]'+ fout_gexf)
    return True


def my_avg_degree(G):
    list_degree = []
    for node in list(G.nodes()):
        list_degree.append(nx.degree(G, node, weight='weight'))
    node_size = G.order()
    avg_degree = sum(list_degree) / node_size
    return avg_degree


def my_max_degree(G):
    max_degree = 0
    for node in list(G.nodes):
        if G.degree(node) > max_degree:
            max_degree = G.degree(node)
    print('max_degree %d' % max_degree)
    return max_degree


def my_max_degree_node(G):
    max_node = {}
    max_degree = 0
    for node in list(G.nodes):
        if G.degree(node) > max_degree:
            max_node = node
            max_degree = G.degree(node)
    print('max_node %s' % max_node)
    return max_node


def my_min_degree(G):
    flag_first = False
    min_degree = 0
    min_node = {}
    for node in list(G.nodes):
        if G.degree(node) < min_degree or flag_first == False:
            min_degree = G.degree(node)
            min_node = node
            flag_first = True
    print('min_degree %d' % min_degree)
    print('%s has min_degree' % min_node)
    return min_degree


def my_PrintFile(f_input_file_name, f_output_file_name):
    print('Input File Name: ' + f_input_file_name)
    print('Output File Name: ' + f_output_file_name)


def my_PrintOutFile(f_output_file_name):
    print('Output File Name: ' + f_output_file_name)


def my_PrintTag(tag_PR, tag_ALGO):
    print('========[PR:' + tag_PR + '][ALGO:' + tag_ALGO + ']  RESULT: SUCCESS========')

#


def my_dict2csv(dict_original, f_out_csv):
    write_file = csv.writer(outputFile)
    with open(f_out_csv, 'w', newline='') as outputFile:
        for key in dict_original.keys():
            value = dict_original[key]
            write_file.writerow([key, value])
    my_PrintOutFile(f_out_csv)

# this function takes an dictionary with node and metric value and store top 10 result in a csv


def my_dicsort2csv(dict_original, f_out_csv, en_reverse, tag_ALGO):
    dict_name = {}
    dict_order = {}
    idx = 0
    for node in dict_original.keys():
        idx = idx + 1
        dict_order[idx] = dict_original[node]
        dict_name[idx] = node

    list_sorted = sorted(dict_order.items(), key=lambda kv: (kv[1], kv[0]), reverse=en_reverse)

    with open(f_out_csv, 'w', newline='') as outputFile:
        write_file = csv.writer(outputFile)
        for i in range(0, 10):
            x = list_sorted[i]
            print(x)
            node = dict_name[x[0]]
            value = dict_original[node]
            write_file.writerow([node, value])
            print('%s has %s  %f :' % (node, tag_ALGO , value))
            if value != x[1]:
                print('dictionary lookup error')
    my_PrintOutFile(f_out_csv)


# print top 10 value to csv
def my_dictop2csv(dict_original, f_out_csv, tag_ALGO):
    my_dicsort2csv(dict_original, f_out_csv, True, tag_ALGO)


# print least 10 value to csv
def my_dicleast2csv(dict_original, f_out_csv, tag_ALGO):
    my_dicsort2csv(dict_original, f_out_csv, False, tag_ALGO)


# add attribute to node and return a node
def my_addattr2node(G, dict_attribute, f_out_gexf, tag_ALGO):
    nG = G.copy()
    for node in dict_attribute.keys():
        nG.nodes[node][tag_ALGO] = dict_attribute[node]
    nx.write_gexf(nG, f_out_gexf)
    return nG


# save histogram plot
def my_plothist(list_in, tag_title, tag_x, tag_y, fout_png):

    plt.cla()  # clear previous plot
    # the histogram of the data
    n, bins, patches = plt.hist(list_in, 40, density=True, facecolor='g', alpha=0.75)

    plt.xlabel(tag_x)
    plt.ylabel(tag_y)
    plt.title(tag_title)
    plt.grid(True)
    #plt.show()
    plt.savefig(fout_png)
    print('[Output]' + fout_png)
    return True


# save scatter plot with control flag en_log
def my_scatterplot(list_x, list_y, tag_title, tag_x, tag_y, fout_png, en_loglog):

    plt.cla()  # clear previous plot
    if en_loglog:
        plt.loglog(list_x, list_y, 'ro')
    else:
        plt.plot(list_x, list_y, 'ro')

    plt.xlabel(tag_x)
    plt.ylabel(tag_y)
    plt.title(tag_title)

    plt.grid(True)
    plt.savefig(fout_png)
    print('[Output]' + fout_png)
    return True


def my_plothist_ex():
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    # the histogram of the data
    n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)
    tag_avg = 10
    print(n)

    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    # plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.xlim(40, 160)
    plt.ylim(0, 0.03)
    plt.grid(True)
    plt.show()
    return True
