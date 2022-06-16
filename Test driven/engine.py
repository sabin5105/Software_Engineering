import pandas as pd

import cleanse


def similar_foods(df, name, n):
    """비슷한 음식 n개 찾기"""
    pref = df.loc[name]
    foods = recommend_foods(df, pref, n + 1)
    return foods[1:]


def recommend_foods(df, pref, n):
    """선호에 맞는 음식 n개 추천하기"""
    diffs_df = df - pref
    distances = (diffs_df**2).sum(axis=1)**0.5
    sorted_distances = distances.sort_values()
    return sorted_distances[:n]


def load_data():
    """음식 데이터를 모두 불러온다"""
    name2gid = {
        '매운맛': 0,
        '기름진맛': 1369311762,
        '단맛': 1090863632,
    }
    dfs = [_fetch_food_data(gid) for gid in name2gid.values()]
    return cleanse.cleanse_and_merge(dfs, name2gid.keys())


def _fetch_food_data(gid):
    """구글시트의 음식 데이터를 pd.DataFrame 형태로 읽어온다"""
    url = \
        'https://docs.google.com/spreadsheets/d/e/' \
        '2PACX-1vSiAzsjRqvLWoFSpOuRlz2xtDef2yAN77AGs' \
        'vmAgCWRtpF8NVr71sNTdNazri4o1FAmF7QA540PNveb' \
        f'/pub?single=true&output=csv&gid={gid}'
    return pd.read_csv(url, index_col=0)
