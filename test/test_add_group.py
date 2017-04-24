from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="name_test1", header="header_test1", footer="footer_test1"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
