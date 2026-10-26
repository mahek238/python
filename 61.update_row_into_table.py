import mysql.connector
cnx = mysql.connector.connect(user='root', password='pwd',
host='127.0.0.1', database='testdb')
cur = cnx.cursor()
cur.execute('UPDATE tbl SET name=%s WHERE id=%s', ('Bob', 1))
cnx.commit()
cur.close(); cnx.close()