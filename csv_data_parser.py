import csv
input_file_name = 'data/example_data.csv'
output_file_name = 'data/example_out.csv'
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
    write_File.writerow([row[10],row[7]]) #loser to winner