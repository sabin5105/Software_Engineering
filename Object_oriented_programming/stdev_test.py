import stdev


def test_stdev():
    pass


def test_exception():
    try:
        stdev.stdev([])
        assert False
    except ValueError as e:
        assert str(e) == "It requires at least one data point to calculate the average."