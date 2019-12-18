import csv

fTag = 'PARSING CSV'
input_ex_file_name = 'data/example_data.csv'
output_ex_file_name = 'data/example_out.csv'

input_file_name = 'data/match_scores_2017_unindexed_csv.csv'
output_file_name = 'data/parse_match_scores_2017.csv'
i = 0

with open(input_file_name, newline='') as inputFile, open(output_file_name, 'w', newline='') as outputFile:

  read_file = csv.reader(inputFile)
  write_File = csv.writer(outputFile)
  # TODO double check list content with "winner_name" "loser_name"
  # TODO maybe using winner_player_id or loser_player_id is better

  # skiping the first row
  iter_rows = iter(read_file)
  next(iter_rows)

  for row in iter_rows:
    print(row)
    print(len(row))
    i = i + 1
    write_File.writerow([row[10],row[7]]) #loser to winner

print('========['+fTag+'] RESULT: SUCCESS========')
print('Input File Name: ' + input_file_name)
print('Output File Name: ' + output_file_name)
print('Number of Entries: ', i)
