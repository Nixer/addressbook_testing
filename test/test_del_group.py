from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    oldgroups = app.group.get_group_list()
    app.group.delete_first_group()
    newgroups = app. group.get_group_list()
    assert len(oldgroups) - 1 == len(newgroups)
    oldgroups[0:1] = []
    assert oldgroups == newgroups
