import pymysql
import pymysql.cursors
from model.group import Group
from fixture.orm import ORMFixture

db = ORMFixture(host="17.218.71.53", user="root", password="", name="addressbook")

# try:
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()

try:
    l = db.get_contacts_not_in_group(Group(id="318"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
