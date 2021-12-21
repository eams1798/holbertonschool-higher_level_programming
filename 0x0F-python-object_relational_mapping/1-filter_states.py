#!/usr/bin/python3
"""lists all states with a name starting with `N`"""


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
    cur.execute("""SELECT * FROM states
                WHERE name LIKE 'N%'
                ORDER BY id ASC""")
    for row in cur.fetchall():
        if row[1][0] == 'N':
            print(row)

    db.close()
