def average(xs):
    try:
        return sum(xs) / len(xs)
    except ZeroDivisionError as e:
        raise ValueError("It requires at least one data point to calculate the average.") from e


def stdev(xs):
    ave = average(xs)
    return (sum([(x - ave)**2 for x in xs]) / len(xs))**0.5

print(stdev((1,2,3)))
print(stdev((0,2,4)))