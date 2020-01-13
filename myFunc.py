import networkx as nx
import csv

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


def my_dictop2csv(dict_original, f_out_csv, en_reverse):
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
            print('%s has harmonic %f :' % (node, value))
            if value != x[1]:
                print('dictionary lookup error')
    my_PrintOutFile(f_out_csv)

