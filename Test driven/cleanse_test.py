import cleanse as c

# does min-max scale works?
def test_min_max_scale_works_correct():
    df = c.make_dummy(
        [
            [1,4,7],
            [2,5,8],
            [3,6,9]
        ], 
        ['a','b','c'])
    actual = c.scale_minmax(df)
    expected = c.make_dummy(
        [
            [0,0,0],
            [0.5,0.5,0.5], 
            [1,1,1]
        ], 
        ['a','b','c'])
    assert actual.eq(expected).all(axis=None)

# drop invalid columns
def test_drop_invalid_columns():
    df = c.make_dummy(
        [
            [1,4,7],
            [2,5,7],
            [3,6,7]
        ], 
        ['a','b','c'])
    actual = c.scale_minmax(df)
    expected = c.make_dummy(
        [
            [0,0],
            [0.5,0.5], 
            [1,1]
        ], 
        ['a','b','c'])
    assert actual.eq(expected).all(axis=None)


def test_empty_df():
    df = c.make_dummy([], [])
    actual = c.scale_minmax(df)
    expected = c.make_dummy([], [])
    assert actual.eq(expected).all(axis=None)


def test_drop_all_columns():
    df = c.make_dummy(
        [
            [1],
            [1],
            [1],
        ],
        ['a', 'b', 'c'],
    )
    actual = c.scale_minmax(df)
    expected = c.make_dummy([], [])
    assert actual.eq(expected).all(axis=None)