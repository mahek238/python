import mysql.connector
# -----------------------------------
# STEP 1: CONNECT TO MYSQL SERVER
# -----------------------------------
conn = mysql.connector.connect(
host="localhost",
user="root",
password=""
)
cursor = conn.cursor()
print("MySQL Connected Successfully")
# -----------------------------------
# STEP 2: CREATE DATABASE
# -----------------------------------
cursor.execute(
"CREATE DATABASE IF NOT EXISTS studentdb"
)
print("Database Created Successfully")
# -----------------------------------
# STEP 3: USE DATABASE
# -----------------------------------
cursor.execute(
"USE studentdb"
)
# -----------------------------------
# STEP 4: CREATE TABLE
# -----------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
id INT AUTO_INCREMENT PRIMARY KEY,
firstname VARCHAR(100),
lastname VARCHAR(100),
mobile VARCHAR(15),
email VARCHAR(100)
)
""")
print("Table Created Successfully")
# -----------------------------------
# STEP 5: INSERT DATA (CREATE)
# -----------------------------------
insert_query = """
INSERT INTO students
(firstname, lastname, mobile, email)
VALUES (%s, %s, %s, %s)
"""
insert_values = (
"Yash",
"Kotecha",
"9876543210",
"yash@gmail.com"
)
cursor.execute(
insert_query,
insert_values
)
conn.commit()
print("Data Inserted Successfully")
# -----------------------------------
# STEP 6: READ DATA
# -----------------------------------
cursor.execute(
"SELECT * FROM students"
)
rows = cursor.fetchall()
print("\n----- STUDENT DATA -----")
for row in rows:
    print(row)
# -----------------------------------
# STEP 7: UPDATE DATA
# -----------------------------------
update_query = """ UPDATE students SET mobile = %s WHERE id = %s"""
update_values = ("9999999999",3)
cursor.execute( update_query, update_values)
conn.commit()
print("\nData Updated Successfully")
# -----------------------------------
# STEP 8: READ UPDATED DATA
# -----------------------------------
cursor.execute(
"SELECT * FROM students"
)
rows = cursor.fetchall()
print("\n----- UPDATED STUDENT DATA -----")
for row in rows:
    print(row)
# -----------------------------------
# STEP 9: DELETE DATA
# -----------------------------------
delete_query = """DELETE FROM students WHERE id = %s """
delete_values = (5,)
cursor.execute(
delete_query,
delete_values
)
conn.commit()
print("\nData Deleted Successfully")
# -----------------------------------
# STEP 10: FINAL READ
# -----------------------------------
cursor.execute(
"SELECT * FROM students"
)
rows = cursor.fetchall()
print("\n----- FINAL STUDENT DATA -----")
for row in rows:
    print(row)
# -----------------------------------
# STEP 11: CLOSE CONNECTION
# -----------------------------------
cursor.close()
conn.close()
print("\nMySQL Connection Closed")