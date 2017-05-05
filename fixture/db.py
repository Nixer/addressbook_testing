import pymysql.cursors
import pymysql
from model.group import Group
from model.contact import Contact


class DBfixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             db=name,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        self.connection.autocommit = True

    def get_group_list(self):
        list =[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                # (id, name, header, footer) = row
                (id, name, header, footer) = (row["group_id"], row["group_name"], row["group_header"], row["group_footer"])
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list =[]
        cursor = self.connection.cursor()
        try:
            cursor.execute('SELECT id, firstname, lastname FROM addressbook WHERE deprecated="0000-00-00 00:00:00"')
            for row in cursor:
                # (id, name, header, footer) = row
                (id, firstname, lastname) = (row["id"], row["firstname"], row["lastname"])
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close