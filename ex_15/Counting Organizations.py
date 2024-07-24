import sqlite3

#Connect to the SQLite database
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

#Create table for organizations and their counts
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if not fname:
    fname = 'mbox.txt'  
try:
    fh = open(fname)
except FileNotFoundError:
    print("File not found, please check the filename and try again.")
    exit()

for line in fh:
    if not line.startswith('From: '): 
        continue
    pieces = line.split()
    if len(pieces) < 2:  
        print("Skipping malformed line:", line.strip())
        continue
    email = pieces[1]
    org = email.split('@')[-1]  

    #Check if the organization already exists in the database
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

#Close the cursor and connection
cur.close()
conn.close()
