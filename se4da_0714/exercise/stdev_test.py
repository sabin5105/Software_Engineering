from exercise import stdev


def test_stdev():
    assert stdev.stdev([1, 2, 3]) == stdev.stdev([3, 4, 5])
    assert 0 < stdev.stdev([1, 2, 3]) < stdev.stdev([0, 2, 4]) < 2


def test_exception():
    try:
        stdev.stdev([])
        assert False
    except ValueError as e:
        assert str(e) == 'Requires at least one data point'
