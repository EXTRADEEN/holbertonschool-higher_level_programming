#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    ''' connect to MySQL server running on localhosh at port 3306 '''
    
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    ''' execute SQL query to retrieve all states '''

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    ''' print results in the desired format '''

    for state in cur.fetchall():
        print(state)

    ''' close database connection '''

    db.close()