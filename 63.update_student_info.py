import mysql.connector
cnx = mysql.connector.connect(user='root', password='pwd',
host='127.0.0.1', database='dbStudent')
cur = cnx.cursor()
cur.execute('UPDATE tblStudInfo SET remarks=%s WHERE student_id=%s',
('Excellent', 1))
cnx.commit()
cur.close(); cnx.close()