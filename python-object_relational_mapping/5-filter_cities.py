#!/usr/bin/python3
"""
 script that takes in the name of a state as an argument and lists all cities
 of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        port=3606,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    state_name_searched = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities "
                "INNER JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.id ASC", (state_name_searched, ))

    city = cur.fetchall()
    cities = [row[0]for row in city]
    string_cities = ', '.join(cities)
    print(string_cities)

    cur.close()
    db.close()
