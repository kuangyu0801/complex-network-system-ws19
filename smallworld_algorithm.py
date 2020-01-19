from myFunc import *
from clustering_algorithm import *
from degree_distribution_algorithm import *

tag_PR = 'PR4b'
tag_ALGO = 'smallworld'
fin_gexf = 'data/Graph_atp_match_2017.gexf'
#  fout_top10_csv = 'output/degree_top10.csv'
m_degree = 10
fout_gexf = 'output/gexf/' + tag_PR + '_' + tag_ALGO + '_m_' + str(m_degree) + '.gexf'