from model.group import Group


def test_add_group(app, db, json_groups):
    group = json_groups
    oldgroups = db.get_group_list()
    app.group.create(group)
    newgroups = db.get_group_list()
    oldgroups.append(group)
    assert sorted(oldgroups, key=Group.id_or_max) == sorted(newgroups, key=Group.id_or_max)
