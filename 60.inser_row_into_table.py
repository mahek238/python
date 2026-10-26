import mysql.connector
cnx = mysql.connector.connect(user='root', password='pwd',
host='127.0.0.1', database='testdb')
cur = cnx.cursor()
cur.execute('INSERT INTO tbl (name) VALUES (%s)', ('Alice',))
cnx.commit()
cur.close(); cnx.close()