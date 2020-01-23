import networkx as nx

print(list(range(1, 20)))
print(list(range(1996, 2017)))

list_year = list(range(1996, 2017))
print(list_year)
list_test = [2017]
print(list_test)
input_file_name = 'data/match_scores_2017_unindexed_csv.csv'
output_file_name = 'data/test.csv'
tag = '2015-197'
info = int(tag[0:4])
print(info)
if info in list_year:
    print('yes')
else:
    print('no')
