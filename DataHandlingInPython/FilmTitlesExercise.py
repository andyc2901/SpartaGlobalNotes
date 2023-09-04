import csv

with open('imdbtitles.csv', newline='') as imdb_data:
    imdb_csv = csv.reader(imdb_data, delimiter=',')
    movies = []
    for data in imdb_csv:
        if data[0] == 'movie' and int(data[4]) >= 2010:
            movie = [data[0], data[1], data[4], data[6], data[7]]
            movies.append(movie)

    for row in movies:
        if 'N' in row[3]:
            row[3] = 'Unknown'

    print(movies)

with open('film_database.csv', 'w', newline='') as output:
    csv_writer = csv.writer(output)
    csv_writer.writerows(movies)
