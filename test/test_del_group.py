from model.group import Group
import random

def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    oldgroups = db.get_group_list()
    group = random.choice(oldgroups)
    app.group.delete_group_by_id(group.id)
    newgroups = db.get_group_list()
    assert len(oldgroups) - 1 == len(newgroups)
    oldgroups.remove(group)
    assert oldgroups == newgroups
    if check_ui:
        assert sorted(newgroups, key=Group.id_or_max()) == sorted(app.group.get_group_list(), key=Group.id_or_max())
