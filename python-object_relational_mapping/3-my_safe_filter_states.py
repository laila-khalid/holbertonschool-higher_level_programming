#!/usr/bin/python3
"""Safe from MySQL injections"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
        (sys.argv[4],)
    )
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
