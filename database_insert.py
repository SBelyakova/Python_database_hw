import sqlalchemy
import psycopg2
from pprint import pprint


engine = sqlalchemy.create_engine('postgresql://postgres:123456789@localhost:5432/music')
pprint(engine)

connection = engine.connect()
print(connection)
pprint(engine.table_names())

# insert_genre = connection.execute('''INSERT INTO genre(name)
#     VALUES ('genre_1'), ('genre_2'), ('genre_3'), ('genre_4'), ('genre_5');
# ''')

insert_genre_check = connection.execute('''SELECT * FROM genre;
''').fetchall()
pprint(insert_genre_check)

# insert_artists = connection.execute('''INSERT INTO artist(name, genreid)
#     VALUES ('artist_1', 11), ('artist_2', 11), ('artist_3', 13), ('artist_4', 12),
#     ('artist_5', 15), ('artist_6', 15), ('artist_7', 14), ('artist_8', 12);
# ''')

insert_artists_check = connection.execute('''SELECT * FROM artist;
''').fetchall()
pprint(insert_artists_check)

# insert_albums = connection.execute(f'''INSERT INTO album(name, releasedate, artistid)
#     VALUES ('album_name_1', '2007-11-02 13:15:20', 17),
#             ('album_name_2', '2007-11-02 13:15:20', 18),
#             ('album_name_3', '2005-11-02 13:15:20', 18),
#             ('album_name_4', '2008-11-02 13:15:20', 19),
#             ('album_name_5', '2012-11-02 13:15:20', 20),
#             ('album_name_6', '2019-11-02 13:15:20', 23),
#             ('album_name_7', '2018-11-02 13:15:20', 20),
#             ('album_name_8', '2018-11-02 13:15:20', 24);
# ''')

insert_album_check = connection.execute('''SELECT * FROM album;
''').fetchall()
pprint(insert_album_check)

# insert_tracks = connection.execute('''INSERT INTO track(name, tracklength, albumid)
#     VALUES ('Track_1', 02.35, 1), ('Track_2', 02.50, 1), ('Track_3', 01.35, 2),
#     ('Track_4', 03.01, 2), ('Track_5', 04.01, 3), ('Track_6', 01.31, 3),
#     ('Track_7', 03.08, 5), ('Track_8', 03.15, 8), ('Track_9', 02.345, 4),
#     ('Track_10', 02.05, 7), ('Track_11', 02.48, 8), ('Track_12', 02.12, 4),
#     ('Track_13', 06.12, 8), ('Track_14', 05.06, 7), ('Track_15', 02.18, 5);
# ''')

insert_tracks_check = connection.execute('''SELECT * FROM track;
''').fetchall()
pprint(insert_tracks_check)

# insert_collections = connection.execute('''INSERT INTO
#     collections(name, release_year)
#     VALUES ('collection_1', '2000-08-27 13:30:02'),
#     ('collection_2', '2010-01-20 13:30:02'),
#     ('collection_3', '2001-11-05 13:30:02'),
#     ('collection_4', '2018-10-25 13:30:02'),
#     ('collection_5', '2013-07-23 13:30:02'),
#     ('collection_6', '2020-12-01 13:30:02'),
#     ('collection_7', '2018-09-10 13:30:02'),
#     ('collection_8', '2011-10-22 13:30:02');
# ''')

insert_collections_check = connection.execute('''SELECT * FROM collections;
''').fetchall()
pprint(insert_collections_check)

# insert_album_artist = connection.execute('''INSERT INTO
#     album_artist(artist_id, album_id)
#     VALUES (17, 1),
#         (17, 2),
#         (22, 3),
#         (23, 4),
#         (24, 5),
#         (19, 6),
#         (18, 7),
#         (20, 8),
#         (18, 8);
# ''')

insert_album_artist_check = connection.execute('''SELECT * FROM album_artist;
''').fetchall()
pprint(insert_album_artist_check)

# insert_artist_genre = connection.execute('''INSERT INTO
#     artist_genre(genre_id, artist_id)
#     VALUES (11, 17),
#     (11, 18),
#     (13, 19),
#     (12, 20),
#     (15, 21),
#     (15, 22),
#     (14, 23),
#     (12, 24);
# ''')

insert_artist_genre_check = connection.execute('''SELECT * FROM artist_genre;
''').fetchall()
pprint(insert_artist_genre_check)

# insert_collections_album_track = connection.execute('''INSERT INTO
#     collections_album_track(collections_id, album_id, track_id)
#     VALUES (1, 3, 5),
#             (2, 1, 2),
#             (3, 2, 3),
#             (4, 4, 12),
#             (5, 5, 7),
#             (6, 7, 10),
#             (7, 8, 11),
#             (8, 4, 9);
#     ''')

insert_collections_album_track_check = connection.execute('''SELECT * FROM collections_album_track;
''').fetchall()
pprint(insert_collections_album_track_check)

# insert_tracks = connection.execute('''INSERT INTO track(name, tracklength, albumid)
#     VALUES ('Track_my', 05.35, 1),
#     ('my apocalypse', 02.50, 1),
#     ('die die die my darling', 01.38, 2);
# ''')
