#!/usr/bin/python3
""" Select * States """
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM \
    cities INNER JOIN states ON state_id = states.id")
    result = cursor.fetchall()

    for x in result:
        print(x)

    cursor.close()
    db.close()
