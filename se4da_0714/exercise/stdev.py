def average(xs):
    try:
        return sum(xs) / len(xs)
    except ZeroDivisionError as e:
        raise ValueError('Requires at least one data point') from e


def stdev(xs):
    mu = average(xs)
    return (sum((xi - mu)**2 for xi in xs) / len(xs))**0.5
