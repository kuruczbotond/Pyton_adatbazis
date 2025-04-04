from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root',
                                 host='127.0.0.1',
                               database='oscar')
cursor = cnx.cursor()
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

print("-----------------------------------------------------")
cursor.execute("SELECT cim, nyert FROM film WHERE nyert > 0")
for film in cursor:
    print(film)
print("-----------------------------------------------------")

cursor.execute("SELECT ev FROM film WHERE COUNT(ev) > 9")
for film in cursor:
    print(film)