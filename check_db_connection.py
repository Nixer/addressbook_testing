import pymysql
import pymysql.cursors
from model.group import Group

connection = pymysql.connect(host="17.218.71.53",
                             user="root",
                             password="",
                             db="addressbook",
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
# try:
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()

list = []
cursor = connection.cursor()
try:
    cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
    for row in cursor:
        print(row)
        (id, name, header, footer) = (row["group_id"], row["group_name"], row["group_header"], row["group_footer"])
        print(id, name, header, footer)
        list.append(Group(name=name, header=header, footer=footer, id=str(id)))
finally:
    cursor.close()
print(list)