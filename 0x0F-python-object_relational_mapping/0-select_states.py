#!/usr/bin/python3
import MySQLdb
import sys
db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY id")
result = cursor.fetchall()

for x in result:
    print(x)
