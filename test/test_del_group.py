from random import randrange
from model.group import Group


def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    oldgroups = app.group.get_group_list()
    index = randrange(len(oldgroups))
    app.group.delete_group_by_index(index)
    newgroups = app. group.get_group_list()
    assert len(oldgroups) - 1 == len(newgroups)
    oldgroups[index:index + 1] = []
    assert oldgroups == newgroups
