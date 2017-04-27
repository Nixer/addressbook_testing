from random import randrange
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    oldgroups = app.group.get_group_list()
    index = randrange(len(oldgroups))
    group = Group(name="New group")
    group.id = oldgroups[index].id
    app.group.modify_group_by_index(index, group)
    newgroups = app.group.get_group_list()
    assert len(oldgroups) == len(newgroups)
    oldgroups[index] = group
    assert sorted(oldgroups, key=Group.id_or_max) == sorted(newgroups, key=Group.id_or_max)

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    oldgroups = app.group.get_group_list()
    index = randrange(len(oldgroups))
    app.group.modify_group_by_index(index, Group(header="New header"))
    newgroups = app.group.get_group_list()
    assert len(oldgroups) == len(newgroups)


