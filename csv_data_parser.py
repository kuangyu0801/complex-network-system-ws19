import csv

fTag = 'PARSING CSV'
input_ex_file_name = 'data/example_data.csv'
output_ex_file_name = 'data/example_out.csv'

input_file = ('data/match_scores_1991-2016_unindexed_csv.csv', 'data/match_scores_2017_unindexed_csv.csv')
output_file = ('data/parse_match_scores_1996-2016.csv','data/parse_match_scores_1991-2016.csv','data/parse_match_scores_2017.csv')
list_year = list(range(1997, 2017))  # from 1996 to 2016
i = 0
input_csv = input_file[0]
output_csv = output_file[0]
print(input_csv)
with open(input_csv, newline='') as inputFile, open(output_csv, 'w', newline='') as outputFile:

    read_file = csv.reader(inputFile)
    write_File = csv.writer(outputFile)

    # skiping the first row
    iter_rows = iter(read_file)
    next(iter_rows)

    for row in iter_rows:
        year_tag = row[0]
        year = year_tag[0:4]
        if int(year) in list_year:
            i = i + 1
            write_File.writerow([row[12].upper(), row[9].upper()]) #loser to winner

print('========['+fTag+'] RESULT: SUCCESS========')
print('Input File Name: ' + input_csv)
print('Output File Name: ' + output_csv)
print('Number of Entries: ', i)
