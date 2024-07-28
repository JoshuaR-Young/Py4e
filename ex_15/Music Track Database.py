import sqlite3
import csv

def create_db():
    conn = sqlite3.connect('tracks.sqlite')
    cur = conn.cursor()

    # Drop tables if they exist to start fresh
    cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;

    CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT UNIQUE
    );

    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    );
    ''')
    print('Database initialized.')
    return conn, cur

def insert_data(conn, cur, file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            artist = row['Artist']
            genre = row['Genre']
            album = row['Album']
            track = row['Name']
            length = int(row['Total Time'])
            rating = int(row['Rating'])
            count = int(row['Play Count'])

            cur.execute('''INSERT OR IGNORE INTO Artist (name) 
                VALUES ( ? )''', (artist, ))
            cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
            artist_id = cur.fetchone()[0]

            cur.execute('''INSERT OR IGNORE INTO Genre (name) 
                VALUES ( ? )''', (genre, ))
            cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
            genre_id = cur.fetchone()[0]

            cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
                VALUES ( ?, ? )''', (album, artist_id))
            cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
            album_id = cur.fetchone()[0]

            cur.execute('''INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) 
                VALUES ( ?, ?, ?, ?, ?, ? )''', 
                (track, album_id, genre_id, length, rating, count))

        conn.commit()
        print('Data inserted into database.')

def query_db(cur):
    cur.execute('''
    SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.id and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
    ''')
    results = cur.fetchall()
    for result in results:
        print(result)

def main():
    conn, cur = create_db()
    insert_data(conn, cur, 'tracks.csv')
    query_db(cur)
    conn.close()

if __name__ == '__main__':
    main()
