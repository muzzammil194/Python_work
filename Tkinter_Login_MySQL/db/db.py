import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="askin"
)

cursor = con.cursor()

#make a function to access the db
def user_login(tup):
    try:
        cursor.execute("SELECT * FROM `admin_table` WHERE `email`=%s AND `password`=%s",tup)
        return (cursor.fetchone())
    except:
        return False
