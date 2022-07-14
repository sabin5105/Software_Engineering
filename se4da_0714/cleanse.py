from statistics import mean

import pandas as pd


def cleanse_and_merge(dfs, names):
    means = [scale_minmax(df).fillna(0.5).mean(axis=1) for df in dfs]
    return pd \
        .concat(means, axis=1, keys=names) \
        .dropna()


def scale_minmax(df):
    """min-max scaling 적용하고 min-max가 같은 칼럼은 제거하기"""
    min_value = df.min()
    max_value = df.max()
    extent = max_value - min_value

    scaled_df = (df - min_value) / extent
    columns_to_keep = extent > 0
    return scaled_df.loc[:, columns_to_keep]


def check_range(df):
    lbound = 0.0
    ubound = 1.0
    df_mask = df.isna()
    df_filled = df.mask(df_mask, mean([lbound, ubound]))

    in_lbound = (df_filled >= lbound).all(axis=None)
    in_ubound = (df_filled <= ubound).all(axis=None)
    return in_lbound and in_ubound


def check_no_na(df):
    return not df.isna().any(axis=None)


def check_foodnames(dfs):
    sets = [set(df.index) for df in dfs]
    return set.intersection(*sets) == set.union(*sets)


def make_dummy(values, names):
    return pd.DataFrame(values, index=names)
