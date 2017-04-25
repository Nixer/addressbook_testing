from model.group import Group


def test_add_group(app):
    oldgroups = app.group.get_group_list()
    app.group.create(Group(name="name_test1", header="header_test1", footer="footer_test1"))
    newgroups = app.group.get_group_list()
    assert len(oldgroups) + 1 == len(newgroups)


def test_add_empty_group(app):
    oldgroups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    newgroups = app.group.get_group_list()
    assert len(oldgroups) + 1 == len(newgroups)