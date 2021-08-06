#!/usr/bin/python3
'''
Script that lists all cities from the database hbtn_0e_4_usa
5-filter_cities.py'''
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()

    cursor.execute('SELECT cities.name FROM cities JOIN states ON\
                    state_id=states.id WHERE states.name = %s\
                    ORDER BY cities.id ASC', [argv[4]])

    print(', '.join([i[0] for i in cursor.fetchall()]))

    cursor.close()
    db.close()
