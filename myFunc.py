import networkx as nx

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

def my_PrintTag(tag_PR, tag_ALGO):
    print('========[PR:' + tag_PR + '][ALGO:' + tag_ALGO + ']  RESULT: SUCCESS========')

def my_topcsv(dict_in, f_out):



