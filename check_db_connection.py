import pymysql
import pymysql.cursors

connection = pymysql.connect(host="17.218.71.53",
                             user="root",
                             password="",
                             db="addressbook",
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()
