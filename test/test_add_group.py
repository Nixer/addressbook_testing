from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("head", 20), footer=random_string("foot", 20))
    for name in range(5)
]


@pytest.mark.parametrize('group', testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    oldgroups = app.group.get_group_list()
    app.group.create(group)
    assert len(oldgroups) + 1 == app.group.count()
    newgroups = app.group.get_group_list()
    oldgroups.append(group)
    assert sorted(oldgroups, key=Group.id_or_max) == sorted(newgroups, key=Group.id_or_max)
