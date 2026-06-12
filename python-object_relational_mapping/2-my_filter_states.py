#!/usr/bin/python3
"""List states matching a user-provided name from a MySQL database."""

import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = db.cursor()

    query = (
        "SELECT * FROM states "
        "WHERE name = '{}' "
        "ORDER BY id ASC"
    ).format(state_name)

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
