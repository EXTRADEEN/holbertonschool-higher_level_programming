#!/usr/bin/python3
''' script that lists all states with a name starting
    with N (upper N) from the database hbtn_0e_0_usa
'''

import MySQLdb
import sys

if __name__ == "__main__":

    ''' connect to MySQL server running on localhosh at port 3306 '''

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    ''' Executing a SELECT query to get all the states whose name
        starts with 'N' in case-sensitive manner
    '''

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                "ORDER BY states.id ASC")

    ''' print results in the desired format '''

    for state in cur.fetchall():
        print(state)

    ''' close database connection '''
    cur.close()
    db.close()
