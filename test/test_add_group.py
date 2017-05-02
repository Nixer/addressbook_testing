from model.group import Group
import pytest
from data.add_group import constant as testdata
# from data.add_group import testdata


@pytest.mark.parametrize('group', testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    oldgroups = app.group.get_group_list()
    app.group.create(group)
    assert len(oldgroups) + 1 == app.group.count()
    newgroups = app.group.get_group_list()
    oldgroups.append(group)
    assert sorted(oldgroups, key=Group.id_or_max) == sorted(newgroups, key=Group.id_or_max)
