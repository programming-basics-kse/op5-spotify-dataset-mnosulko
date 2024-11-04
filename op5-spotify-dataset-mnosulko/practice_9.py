import csv
import ast
from audioop import reverse

lines = []
with open('top_50_2023.csv', 'r') as file:
   columns = next(file)
   for line in file:
       line = line[:-1].split(',')
       lines.append(line)
print(lines[0])
# ARTIST = 0
# for line in lines:
#        print(line[ARTIST])
rows = []
with open('top_50_2023.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    header = next(csv_reader)
    for row in csv_reader:
        rows.append(row)
dance = header.index('danceability')

sum = 0
for row in rows:
    sum += float(row[dance])
print(sum / len(rows))





#number 2
liveliness = header.index('liveness')
energy = header.index('energy')

sum = 0
for row in rows:
    if energy >= 0.5:
        sum+=liveliness
print(sum / len(rows))





#number 3
file_path = 'top_50_2023.csv'
artist_counts = {}

with open(file_path, 'r', encoding='utf-8') as file:

    next(file)
    for line in file:

        artist_name = line.split(',')[0].strip()


        if artist_name in artist_counts:
            artist_counts[artist_name] += 1
        else:
            artist_counts[artist_name] = 1


top_artist = max(artist_counts.items(), key=lambda x: x[1])

print(f"artist whose tracks appear the most in the list: {top_artist[0]}: {top_artist[1]} times")






#number 5:

file_path = 'top_50_2023.csv'
year_counts = {}

with open(file_path, 'r', encoding='utf-8') as file:

    next(file)
    for line in file:

        release_date = line.split(',')[3].strip()

        year = release_date[:4]


        if year in year_counts:
            year_counts[year] += 1
        else:
            year_counts[year] = 1


top_year = max(year_counts.items(), key=lambda x: x[1])

print(f"the year when the most songs were released: {top_year[0]}: {top_year[1]} songs")


