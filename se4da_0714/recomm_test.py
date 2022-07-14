import pandas as pd

from engine import Recommender, load_data
from recomm import History, Shell


def test_parse_raw_input():
    shell = Shell(None, None)
    cases = [
        ("0 0.5 1", [0.0, 0.5, 1.0]),
        ("1 0.0 0.5", [1.0, 0.0, 0.5]),
        ("-1 0.5 2", [0.0, 0.5, 1.0]),
        ("0,0.5,1", [0.0, 0.5, 1.0]),
        ("0, 0.5, 1", [0.0, 0.5, 1.0]),
    ]
    for raw, expected in cases:
        actual = shell.parse_raw_input(raw)
        assert expected == actual


def test_parse_invalid_number():
    shell = Shell(None, None)
    try:
        shell.parse_raw_input('a b c')
        assert False
    except ValueError as e:
        assert str(e) == 'Please enter real number such as 0.5'


def test_parse_empty_input():
    shell = Shell(None, None)
    try:
        shell.parse_raw_input('')
        assert False
    except ValueError as e:
        assert str(e) == 'Please enter something'


def test_describe_recomm():
    shell = Shell(None, None)
    actual = shell.describe_recomm(['짜장', '탕슉'])
    expected = "Recommendations: 짜장, 탕슉"
    assert expected == actual


def test_update_recents():
    history = History()
    recents = ['a', 'b', 'c', 'd']
    new_recomms = ['e', 'f', 'g']
    actual = history._merge(recents, new_recomms, 6)
    expected = ['b', 'c', 'd', 'e', 'f', 'g']
    assert expected == actual
