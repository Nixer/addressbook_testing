from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="1232", header="123312", footer="32312"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
