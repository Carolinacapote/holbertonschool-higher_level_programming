#!/usr/bin/python3
'''
Script that lists all cities from the database hbtn_0e_4_usa
'''
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()

    cursor.execute('SELECT cities.id, cities.name, states.name FROM cities\
                    JOIN states ON state_id=states.id ORDER BY cities.id ASC')

    for i in cursor.fetchall():
        print(i)

    cursor.close()
    db.close()
