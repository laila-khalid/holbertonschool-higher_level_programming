#!/usr/bin/python3
"""All cities by state"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    
    query = (
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = BINARY %s ORDER BY cities.id ASC"
    )
    cursor.execute(query, (sys.argv[4],))
    
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))
    
    cursor.close()
    db.close()
