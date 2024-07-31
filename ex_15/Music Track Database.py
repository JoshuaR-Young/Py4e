import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
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
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Open the tracks.csv file
handle = open('tracks.csv')

# Iterate over each line in the CSV file
for line in handle:
    line = line.strip()
    pieces = line.split(',')
    if len(pieces) < 7:
        continue

    # Extract data from the CSV columns
    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    genre = pieces[3]
    length = pieces[4]
    rating = pieces[5]
    count = pieces[6]

    # Print the extracted data (for debugging purposes)
    print(name, artist, album, genre, length, rating, count)

    # Insert or ignore the artist data
    cur.execute('''
    INSERT OR IGNORE INTO Artist (name) 
    VALUES (?)''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]

    # Insert or ignore the album data
    cur.execute('''
    INSERT OR IGNORE INTO Album (title, artist_id) 
    VALUES (?, ?)''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cur.fetchone()[0]

    # Insert or ignore the genre data
    cur.execute('''
    INSERT OR IGNORE INTO Genre (name) 
    VALUES (?)''', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
    genre_id = cur.fetchone()[0]

    # Insert or replace the track data
    cur.execute('''
    INSERT OR REPLACE INTO Track
    (title, album_id, genre_id, len, rating, count) 
    VALUES (?, ?, ?, ?, ?, ?)''',
    (name, album_id, genre_id, length, rating, count))

    # Commit the changes
    conn.commit()

# Close the file handle
handle.close()
