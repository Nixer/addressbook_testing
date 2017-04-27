from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    oldgroups = app.group.get_group_list()
    group = Group(name="New group")
    group.id = oldgroups[0].id
    app.group.modify_first_group(group)
    newgroups = app.group.get_group_list()
    assert len(oldgroups) == len(newgroups)
    oldgroups[0] = group
    assert sorted(oldgroups, key=Group.id_or_max) == sorted(newgroups, key=Group.id_or_max)

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    oldgroups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header"))
    newgroups = app.group.get_group_list()
    assert len(oldgroups) == len(newgroups)


