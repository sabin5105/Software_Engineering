import pandas as pd

import cleanse


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


class Recommender:

    def __init__(self, df):
        self.df = df

    def by_prefs(self, prefs, n, recents):
        """선호에 맞는 음식 n개 추천하기"""
        # 최근에 추천한 음식은 제외하기
        mask = ~self.df.index.isin(recents)
        masked_df = self.df[mask]

        # 추천할 음식 고르기
        diffs_df = masked_df - prefs
        distances = (diffs_df**2).sum(axis=1)**0.5
        sorted_distances = distances.sort_values()
        new_recomms = sorted_distances[:n].index.tolist()

        return new_recomms

    def by_name(self, name, n):
        """비슷한 음식 n개 찾기"""
        pref = self.df.loc[name]
        foods = self.by_prefs(pref, n + 1, [])
        return foods[1:]
