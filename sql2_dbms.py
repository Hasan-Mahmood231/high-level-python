import mysql.connector

# conn = mysql.connector.connect(host="localhost", user="root", password="yourpassword")
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hasan0342?",
    auth_plugin='mysql_native_password'
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS earth")
cursor.execute("USE earth")
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))")
cursor.execute("INSERT INTO users (name) VALUES ('Aizaz')")
conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

cursor.close()
conn.close()
