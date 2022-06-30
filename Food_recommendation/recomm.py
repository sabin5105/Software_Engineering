import re

import engine


def main():
    print("Welcome to the Food Recommendation System!")
    df = engine.load_data()

    # TODO: read from file
    recents = []
    while True:
        try:
            raw_input = input("Enter your preferences (hot oily sweet): ")
            prefs = parse_raw_input(raw_input)
            foods, recents = engine.recommend_foods(df, prefs, 3, recents)
            print(describe_recomm(foods))
        except ValueError as e:
            print(e)
        except EOFError:
            print("Bye!")
            break

        print()


def parse_raw_input(raw_input):
    if not raw_input:
        raise ValueError('Please enter something')

    try:
        return [
            _clamp(float(token), 0.0, 1.0)
            for token in re.split(r'\s|,\s?', raw_input)
        ]
    except ValueError as e:
        raise ValueError('Please enter real number such as 0.5') from e


def describe_recomm(foods):
    recomm_foods = ', '.join(foods.index.tolist())
    return f"Recommendations: {recomm_foods}"


def _clamp(x, lbound, ubound):
    return min(max(x, lbound), ubound)


if __name__ == '__main__':
    main()
