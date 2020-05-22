import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
from config import db_password


def process_song_file(cur, song_filepath):
    # open song file
    song_df = pd.read_json(song_filepath, lines=True)
    # Rename the columns
    song_df.rename(columns={'artist_id':'artist_id', 
                   'artist_name':'name',
                   'artist_location':'location',
                   'artist_latitude':'latitude',
                   'artist_longitude':'longitude'})

    # insert song record
    song_data = [song_id,title,artist_id,year,duration]
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = [artist_id,name,location,latitude,longitude]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, log_filepath):
    # open log file
    log_df = pd.read_json(log_filepath, lines=True)
    # drop na values
    log_df = log_df.dropna()

    # filter by NextSong action
    time_df = log_df.loc[log_df.page=='NextSong',:]
    
    # convert timestamp column to datetime
    t = pd.to_datetime(time_df['ts'], unit='ms')
    
    # insert time data records
    time_data = []
    for time in t:
        time_data.append([
            time,time.hour,
            time.day,time.week,
            time.month,time.year,
            time.day_name()
        ])
    column_labels = ('start_time','hour','day','week','month','year','weekday')
    time_df = pd.DataFrame.from_records(time_data, columns=column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = log_df[['userId','firstName','lastName','gender','level']].copy()

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in log_df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (
            index, pd.to_datetime(row.ts, unit='ms'), 
            int(row.userId), row.level, songid, artistid, 
            row.sessionId, row.location, row.userAgent
        )
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect(f"host=127.0.0.1 dbname=sparkifydb user=postgres password={db_password}")
    cur = conn.cursor()

    process_data(cur, conn, song_filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, log_filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()