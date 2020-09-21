#!/usr/bin/python

import MySQLdb
db =MySQLdb.connect(host="161.246.34.35",
                    user="k60010063_eiei",
                    passwd="test123",
                    db="k60010063_eiei"
        )

cur = db.cursor()

cur.execute("SELECT * FROM table_name")

for row in cur.fetchall():
    print row[0]

db.close
