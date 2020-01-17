# Main python program: network_analysis.py
# TODO [PR0] making this the main program
from clustering_algorithm import *

fin_gexf = 'data/Graph_atp_match_2017.gexf'
#f_output_dd_csv = 'output/csv/distance_distribution.csv'
#f_output_cc_csv = 'output/csv/cc_distribution.csv'
tag_PR = 'PR2'
tag_ALGO = 'degree_centrality'
#tag_ALGO_1 = 'clustering_coeff'
#fout_top10_csv = 'output/degree_top10.csv'
fout_gexf = 'output/gexf/' + tag_PR +'_'+  tag_ALGO + '.gexf'

my_clustering(fin_gexf, tag_PR)
