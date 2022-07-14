import re

from engine import Recommender, load_data


def main():
    recomm = Recommender(load_data())
    history = History()
    Shell(recomm, history).run()


class Shell:

    def __init__(self, recomm, history):
        self.recomm = recomm
        self.history = history

    def run(self):
        print("Welcome to the Food Recommendation System!")
        try:
            while True:
                raw_input = input("Enter your preferences (hot oily sweet): ")
                output = self.step(raw_input)
                print(output)
                print()
        except EOFError:  # EOF: End-of-file
            print("Bye!")

    def step(self, raw_input):
        try:
            prefs = self.parse_raw_input(raw_input)
            foods = self.recomm.by_prefs(prefs, 3, self.history.get())
            self.history.update(foods, 6)
            return self.describe_recomm(foods)
        except ValueError as e:
            return e

    def parse_raw_input(self, raw_input):
        if not raw_input:
            raise ValueError('Please enter something')

        try:
            return [
                self._clamp(float(token), 0.0, 1.0)
                for token in re.split(r'\s|,\s?', raw_input)
            ]
        except ValueError as e:
            raise ValueError('Please enter real number such as 0.5') from e

    def describe_recomm(self, foods):
        recomm_foods = ', '.join(foods)
        return f"Recommendations: {recomm_foods}"

    def _clamp(self, x, lbound, ubound):
        return min(max(x, lbound), ubound)


class History:
    RECENT_FILENAME = 'recomm.log'

    def get(self):
        with open(History.RECENT_FILENAME, encoding='utf-8') as f:
            return f.read().splitlines()

    def update(self, new_recomms, n):
        merged = self._merge(self.get(), new_recomms, n)
        self._save(merged)

    def _save(self, recents):
        with open(History.RECENT_FILENAME, 'w', encoding='utf-8') as f:
            f.writelines(r + '\n' for r in recents)

    def _merge(self, recents, new_recomms, n):
        return (recents + new_recomms)[-n:]


if __name__ == '__main__':
    main()
