from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root',
                                 host='127.0.0.1',
                               database='kiralyok')

#tablak megjelenítése                        
cursor = cnx.cursor()
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
print("----------------------------------------------------------------------------------------------------")


#uralkodó megjelenítése
cursor.execute("SELECT * FROM uralkodo")
for uralkodo in cursor:
    print(uralkodo)
print("----------------------------------------------------------------------------------------------------")

cursor.execute ("SELECT * FROM uralkodo WHERE nev = 'I. Mátyas'")
for uralkodo in cursor:
    print(uralkodo)
print("----------------------------------------------------------------------------------------------------")

cursor.execute ("SELECT szul, hal FROM uralkodo WHERE nev = 'I. Mátyas'")
for uralkodo in cursor:
    print(f"Máytás király élt: {uralkodo[0]} - {uralkodo[1]}")
print("----------------------------------------------------------------------------------------------------")
cnx.close()