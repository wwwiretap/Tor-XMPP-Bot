import sqlite3
import time
import hashlib

db = sqlite3.connect('doclist') # might need to use self.filename
db.execute("CREATE TABLE IF NOT EXISTS doclist(id text, title text)")
db.commit()
        
thisdate = time.time()
title = 'title'

db.execute('INSERT INTO doclist(id, title) VALUES(?,?)', (thisdate, title))
db.commit()

with db:        
    
    cur = db.cursor()    
    cur.execute('SELECT * FROM doclist')
    
    col_names = [cn[0] for cn in cur.description]
    
    rows = cur.fetchall()
    
    print "%s %s" % (col_names[0], col_names[1])

    for row in rows:    
        print "%s %s" % row
