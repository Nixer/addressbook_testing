from model.group import Group


def test_add_group(app):
    oldgroups = app.group.get_group_list()
    group = Group(name="name_test1", header="header_test1", footer="footer_test1")
    app.group.create(group)
    assert len(oldgroups) + 1 == app.group.count()
    newgroups = app.group.get_group_list()
    oldgroups.append(group)
    assert sorted(oldgroups, key=Group.id_or_max) == sorted(newgroups, key=Group.id_or_max)


def test_add_empty_group(app):
    group = Group(name="", header="", footer="")
    oldgroups = app.group.get_group_list()
    app.group.create(group)
    newgroups = app.group.get_group_list()
    assert len(oldgroups) + 1 == len(newgroups)
    oldgroups.append(group)
    assert sorted(oldgroups, key=Group.id_or_max) == sorted(newgroups, key=Group.id_or_max)
