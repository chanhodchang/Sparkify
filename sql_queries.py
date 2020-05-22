# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay_table"
user_table_drop = "DROP TABLE IF EXISTS user_table"
song_table_drop = "DROP TABLE IF EXISTS song_table"
artist_table_drop = "DROP TABLE IF EXISTS artist_table"
time_table_drop = "DROP TABLE IF EXISTS time_table"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplay_table
(songplay_id int PRIMARY KEY,
start_time date REFERENCES time_table(start_time),
user_id int REFERENCES user_table(user_id),
level varchar,
song_id int REFERENCES song_table(song_id),
artist_id int REFERENCES artist_table(artist_id),
session_id int,
location varchar,
user_agent varchar)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS user_table
(user_id int PRIMARY KEY,
first_name varchar NOT NULL,
last_name varchar NOT NULL,
gender varchar NOT NULL,
level varchar NOT NULL)
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
CREATE TABLE IF NOT EXISTS artist_table(
    artist_id text PRIMARY KEY,
    artist_name text NOT NULL,
    artist_location text,
    artist_latitude float,
    artist_longitude float
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time_table
(start_time date PRIMARY KEY,
hour int NOT NULL,
day int NOT NULL,
week int NOT NULL,
month int NOT NULL,
year int NOT NULL,
weekday varchar NOT NULL)
""")

# INSERT RECORDS

songplay_table_insert = ("""
-- INSERT INTO songplay_table
(songplay_id,start_time,user_id,level,song_id,artist_id,session_id,location,user_agent)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (songplay_id) DO NOTHING;
""")

user_table_insert = ("""
-- INSERT INTO user_table
(user_id,first_name,last_name,gender,level)
VALUES(%s,%s,%s,%s,%s)
ON CONFLICT (user_id) DO NOTHING;
""")

song_table_insert = ("""
INSERT INTO song_table 
(song_id,title,artist_id,year,duration)
VALUES(%s,%s,%s,%s,%s)
ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
-- INSERT INTO artist_table
(artist_id, artist_name, artist_location, artist_latitude,artist_longitude)
VALUES(%s,%s,%s,%s,%s)
ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
-- INSERT INTO time_table
(start_time,hour,day,week,month,year,weekday)
VALUES(%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]