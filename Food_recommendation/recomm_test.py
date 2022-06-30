import recomm
import pandas as pd

def test_parse_raw_input():
    cases = [
        ("0 0.5 1", [0.0, 0.5, 1.0]),
        ("1 0.0 0.5", [1.0, 0.0, 0.5]),
        ("-1 0.5 2", [0.0, 0.5, 1.0]),
        ("-1,0.5,2", [0.0, 0.5, 1.0]),
        ("-1, 0.5, 2", [0.0, 0.5, 1.0]),
    ]
    for raw, expected in cases:
        actual = recomm.parse_raw_input(raw)
        assert expected == actual


def test_parse_invalid_number():
    try:
        recomm.parse_raw_input('a b c')
        assert False
    except ValueError as e:
        assert str(e) == 'Please enter real number such as 0.5'


def test_parse_empty_input():
    try:
        recomm.parse_raw_input('')
        assert False
    except ValueError as e:
        assert str(e) == 'Please enter something'


def test_describe_recomm():
    source = pd.Series({'짜장': 0.0, '탕슉': 0.1})
    actual = recomm.describe_recomm(source)
    expected = "Recommendations: 짜장, 탕슉"
    assert expected == actual


def test_blah():
    with open('test.txt', 'w') as f:
        f.write('Hello world!')