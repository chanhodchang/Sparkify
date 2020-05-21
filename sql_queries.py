# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay_table"
user_table_drop = "DROP TABLE IF EXISTS user_table"
song_table_drop = "DROP TABLE IF EXISTS song_table"
artist_table_drop = "DROP TABLE IF EXISTS artist_table"
time_table_drop = "DROP TABLE IF EXISTS time_table"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplay_table()
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS user_table()
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS song_table
(song_id text PRIMARY KEY, 
title text NOT NULL, 
artist_id text NOT NULL, 
year int, 
duration float NOT NULL)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist_table()
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time_table()
""")

# INSERT RECORDS

songplay_table_insert = ("""
-- INSERT INTO songplay_table()
""")

user_table_insert = ("""
-- INSERT INTO user_table()
""")

song_table_insert = ("""
INSERT INTO song_table 
(song_id,title,artist_id,year,duration)
VALUES(%s,%s,%s,%s,%s)
ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
-- INSERT INTO artist_table()
""")


time_table_insert = ("""
-- INSERT INTO time_table()
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]