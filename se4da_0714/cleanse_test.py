import cleanse as c


def test_scaling():
    df = c.make_dummy(
        [
            [1, 0, -2],
            [2, 0, 0],
            [3, 10, +2],
        ],
        ['a', 'b', 'c'],
    )
    actual = c.scale_minmax(df)
    expected = c.make_dummy(
        [
            [0, 0, 0],
            [0.5, 0, 0.5],
            [1, 1, 1],
        ],
        ['a', 'b', 'c'],
    )
    assert actual.eq(expected).all(axis=None)


def test_drop_invalid_columns():
    df = c.make_dummy(
        [
            [1, 10],
            [2, 10],
            [3, 10],
        ],
        ['a', 'b', 'c'],
    )
    actual = c.scale_minmax(df)
    expected = c.make_dummy(
        [
            [0],
            [0.5],
            [1],
        ],
        ['a', 'b', 'c'],
    )
    assert actual.eq(expected).all(axis=None)


def test_empty_df():
    df = c.make_dummy([], [])
    actual = c.scale_minmax(df)
    expected = c.make_dummy([], [])
    assert actual.eq(expected).all(axis=None)


def test_drop_all_columns():
    df = c.make_dummy(
        [[1], [1], [1]],
        ['a', 'b', 'c'],
    )
    actual = c.scale_minmax(df)
    expected = c.make_dummy([], [])
    assert actual.eq(expected).all(axis=None)
