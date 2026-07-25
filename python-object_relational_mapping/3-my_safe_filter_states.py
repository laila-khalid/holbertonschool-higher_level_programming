#!/usr/bin/python3
"""Safe from MySQL injections"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    
    query = "SELECT * FROM states WHERE name = BINARY %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))
    
    for row in cursor.fetchall():
        print(row)
        
    cursor.close()
    db.close()
