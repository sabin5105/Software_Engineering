import pandas as pd

import cleanse


def similar_foods(df, name, n):
    """비슷한 음식 n개 찾기"""
    pref = df.loc[name]
    foods, _ = recommend_foods(df, pref, n + 1, [])
    return foods[1:]


def recommend_foods(df, pref, n, recents):
    """선호에 맞는 음식 n개 추천하기"""
    # 최근에 추천한 음식은 제외하기
    mask = ~df.index.isin(recents)
    df = df[mask]

    # 추천할 음식 고르기
    diffs_df = df - pref
    distances = (diffs_df**2).sum(axis=1)**0.5
    sorted_distances = distances.sort_values()
    new_recomms = sorted_distances[:n]

    # 최근 추천한 음식 목록 갱신
    new_recents = update_recents(recents, new_recomms.index.tolist(), 6)

    return new_recomms, new_recents


def update_recents(recents, new_recomms, n):
    return (recents + new_recomms)[-n:]


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