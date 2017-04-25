from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    oldgroups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New group"))
    newgroups = app.group.get_group_list()
    assert len(oldgroups) == len(newgroups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    oldgroups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header"))
    newgroups = app.group.get_group_list()
    assert len(oldgroups) == len(newgroups)

