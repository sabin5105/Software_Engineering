from numpy import source
import recomm


def test_parse_raw_input():
    cases = [
        ("0 0.5 1", [0.0, 0.5, 1.0]),
        ("1 0.0 0.5", [1.0, 0.0, 0.5]),
        ("-1 0.5 2", [0.0, 0.5, 1.0]),
    ]
    for raw, expected in cases:
        actual = recomm.parse_raw_input(raw)
        assert expected == actual
    