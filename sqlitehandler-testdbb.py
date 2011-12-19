import sqlite3
import time
import hashlib

db = sqlite3.connect('testdb') # might need to use self.filename
db.execute("CREATE TABLE IF NOT EXISTS testdb(date text, email text, action text)")
db.commit()
        
thisdate = time.time()
action = 'get-request-browser-tor-fa'

hashed = hashlib.sha224("Nobody inspects the sqlite time sql statementspammish repetition").hexdigest()
db.execute('INSERT INTO testdb(date, email,action) VALUES(?,?,?)', (thisdate, hashed, action))
db.commit()

with db:
    
    cur = db.cursor()    
    cur.execute('SELECT * FROM testdb')
    
    col_names = [cn[0] for cn in cur.description]
    
    rows = cur.fetchall()
    
    print "%s %s %s" % (col_names[0], col_names[1], col_names[2])

    for row in rows:    
        print "%s %s %s" % row
