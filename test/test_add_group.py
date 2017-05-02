from model.group import Group


def test_add_group(app, data_groups):
    group = data_groups
    oldgroups = app.group.get_group_list()
    app.group.create(group)
    assert len(oldgroups) + 1 == app.group.count()
    newgroups = app.group.get_group_list()
    oldgroups.append(group)
    assert sorted(oldgroups, key=Group.id_or_max) == sorted(newgroups, key=Group.id_or_max)
