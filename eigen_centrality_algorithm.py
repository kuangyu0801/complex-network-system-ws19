# implementation of eigen centrality algorithm
import networkx as nx
f_input_gexf = 'data/Graph_atp_match_2017.gexf'

node_harm = nx.harmonic_centrality(G, nbunch=None, distance=None)