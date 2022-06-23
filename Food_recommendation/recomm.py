from curses import raw
import engine


def main():
    print("Welcome to the Food Recommendation System!")
    df = engine.load_data()

    while True:
        raw_input = input("Enter your preferences (hot oily sweet): ")
        prefs = parse_raw_input(raw_input)
        foods = engine.recommend_foods(df, prefs, 3)
        print(describe_recomm(foods))
        print()


def parse_raw_input(raw_input):
    return [_clamp(float(token), 0.0, 1.0) for token in raw_input.split()]    # clamping


def _clamp(x, lbound, ubound):
    return max(min(x, ubound), lbound)


def describe_recomm(foods):
    recomm_foods = ', '.join(foods.index.tolist())
    return f"Recommendations: {recomm_foods}"


if __name__ == '__main__':
    main()