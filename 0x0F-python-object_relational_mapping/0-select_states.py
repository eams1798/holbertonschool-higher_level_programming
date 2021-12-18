#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    from sys import argv
    from sys import exit
    import MySQLdb

    if len(argv) != 4:
        exit(0)

    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)

    db.close()
