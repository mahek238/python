import mysql.connector
cnx = mysql.connector.connect(user='root', password='pwd',
host='127.0.0.1', database='dbStudent')
cur = cnx.cursor()
cur.execute('DELETE FROM tblStudInfo WHERE student_id=%s', (1,))
cnx.commit()
cur.close(); cnx.close()