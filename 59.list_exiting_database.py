import mysql.connector
cnx = mysql.connector.connect(user='root', password='pwd',
host='127.0.0.1')
cursor = cnx.cursor()
cursor.execute('SHOW DATABASES')
for db in cursor:
 print(db)
