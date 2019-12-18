import networkx as nx
import matplotlib.pyplot as plt

fTag = 'DRAW GRAPH'
f_ex_input_gexf = 'data/atp_match_graph.gexf'
f_ex_output_pdf = 'pic/ATP_multigraph.pdf'

f_input_gexf = 'data/atp_match_2017_graph.gexf'
f_output_pdf = 'pic/ATP_multigraph_2017.pdf'



G = nx.read_gexf(f_input_gexf)
nx.draw(G, with_labels= True)
plt.savefig(f_output_pdf)

print('========['+fTag+'] RESULT: SUCCESS========')
print('Input GEXF File Name: ' + f_input_gexf)
print('Output PDF File Name: ' + f_output_pdf)