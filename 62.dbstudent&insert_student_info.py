# Create DB and table using MySQL client or python connector.
# Insert example:
import mysql.connector
cnx = mysql.connector.connect(user='root', password='pwd',
host='127.0.0.1')
cur = cnx.cursor()
cur.execute('CREATE DATABASE IF NOT EXISTS dbStudent')
cur.execute('USE dbStudent')
cur.execute('''CREATE TABLE IF NOT EXISTS tblStudInfo (
 student_id INT PRIMARY KEY AUTO_INCREMENT,
 student_name VARCHAR(100),
 stream VARCHAR(50),
 college_name VARCHAR(150),
 contact_number VARCHAR(30),
 remarks TEXT)''')
cur.execute('INSERT INTO tblStudInfo (student_name, stream,college_name, contact_number, remarks) VALUES (%s,%s,%s,%s,%s)',
 ('John Doe','CS','ABC College','9999999999','Good'))
cnx.commit()
cur.close(); cnx.close()
