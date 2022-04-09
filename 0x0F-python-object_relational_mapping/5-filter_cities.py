#!/usr/bin/python3
"filter cities"

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=user, passwd=passwd, db=db)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM states JOIN cities\
        ON states.id = state_id AND states.name LIKE BINARY %s;", (sys.argv[4],))
    result = cursor.fetchall()

    for x in range(len(result)):
        if x == len(result) - 1:
            print(result[x][0])
        else:
            print(result[x][0] + ", ", end="")
