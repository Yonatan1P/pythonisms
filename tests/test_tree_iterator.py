from pythonisms.iterators.tree_iterator import IterableBinaryTree
import string

def test_lowercase_iterable_binary_tree():
    tree = IterableBinaryTree(values=string.ascii_lowercase)
    actual = list(tree)
    expected = ['a','b','d','h','p','q','i','r','s','e','j','t','u','k','v','w','c','f','l','x','y','m','z','g','n','o']
    assert actual == expected

def test_make_uppercase_iterable_binary_tree():
    tree = IterableBinaryTree(values=string.ascii_lowercase)
    actual = [char.upper() for char in tree]
    expected = ['A','B','D','H','P','Q','I','R','S','E','J','T','U','K','V','W','C','F','L','X','Y','M','Z','G','N','O']
    assert actual == expected

def test_find_vowels_in_iterable_binary_tree():
    tree = IterableBinaryTree(values=string.ascii_lowercase)
    actual = [char for char in tree if char.lower() in 'aeiou']
    expected = ['a', 'i', 'e', 'u', 'o']
    assert actual == expected

def test_find_heaviest_in_iterable_tree():
    tree = IterableBinaryTree(values=[
        {'name':'yoni','weight':195},
        {'name':'gahl','weight':165},
        {'name':'John','weight':175},
    ])

    actual = max(tree, key = lambda o: o['weight'])
    expected = {'name': 'yoni', 'weight': 195}
    assert actual == expected

def test_if_all_letters_are_vowels_in_iterable_binary_tree():
    tree = IterableBinaryTree(values=string.ascii_lowercase)
    actual = all([char in 'aeiou' for char in tree])
    expected = False
    assert actual == expected

def test_if_any_a_in_iterable_binary_tree():
    tree = IterableBinaryTree(values=string.ascii_lowercase)
    actual = any([char =='a' for char in tree])
    expected = True
    assert actual == expected