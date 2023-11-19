#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    mb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], mb=sys.argv[3], port=3306)
    czr = mb.cursor()
    czr.execute("SELECT * FROM states")
    rows = czr.fetchall()
    for row in rows:
        print(row)
    czr.close()
    mb.close()
