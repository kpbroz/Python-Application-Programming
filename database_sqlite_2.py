import sqlite3
conn=sqlite3.connect('farooq.sqlite')
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS Animals')
cur.execute('CREATE TABLE Animals(color TEXT,leg INTEGER)')
conn.close()
