#store and print the count of occurence of word in a file

import sqlite3

conn=sqlite3.connect('worddb.sqlite')
cur=conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (word TEXT, count INTEGER)')

fname='romeo.txt'
if (len(fname)<1): fname='romeo.txt'
fh=open(fname)

for line in fh:
    line=line.rstrip()
    words=line.split()
    for word in words:
        cur.execute('SELECT count FROM Counts WHERE word=?',(word,))
        row=cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (word, count) VALUES (?,1)',(word,))
        else:
            cur.execute('UPDATE Counts SET count=count+1 WHERE word=?',(word,))
    conn.commit()
    
sqlstr='SELECT word, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])
    
cur.close()
