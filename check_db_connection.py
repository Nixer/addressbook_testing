import pymysql
import pymysql.cursors
from model.group import Group
from fixture.db import DBfixture

db = DBfixture(host="17.218.71.53", user="root", password="", name="addressbook")

# try:
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()

try:
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()
