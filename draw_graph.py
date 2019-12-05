import networkx as nx
import matplotlib.pyplot as plt

f_input_gexf = 'data/atp_match_graph.gexf'
f_output_pdf = 'pic/ATP_multigraph.pdf'



G = nx.read_gexf(f_input_gexf)
nx.draw(G, with_labels= True)
plt.savefig(f_output_pdf)