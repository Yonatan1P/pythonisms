from pythonisms import __version__
import pytest

from pythonisms.iterators.linked_list_iterator import LinkedList

def test_for_in():
    ll = LinkedList((1,2,3))
    node_list = []
    for node in ll:
        node_list.append(node)

    assert node_list == [1,2,3]

def test_version():
    assert __version__ == '0.1.0'
