#!/usr/bin/python3
"""lists all cities from a state passed as an argument"""


if __name__ == "__main__":
    from sys import argv
    from sys import exit
    import MySQLdb

    if len(argv) != 5:
        exit(0)

    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute(
            "SELECT cities.name FROM cities \
            INNER JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s ORDER BY cities.id ASC", [argv[4]])

    answer = []
    for row in cur.fetchall():
        answer.append(row[0])

    print(", ".join(answer))

    db.close()
