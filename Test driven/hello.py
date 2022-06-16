def hello(names):
    if len(names) == 0:
        return "Hello World!"

    if len(names) > 1:
        joined = ', '.join(names[:-1]) + (f' and {names[-1]}')
        temp = joined

    else:
        temp = names[0]   
    return f"Hello {temp}!"


def hello_2(names):
    if len(names) == 0:
        parts = ['World']

    if len(names) == 1:
        parts = names

    else:
        parts = [', '.join(names[:-1]), names[-1]]
        
    return f"Hello {' and '.join(parts)}!"


if __name__ == '__main__':
    print(hello(['Alan', 'Brad', 'Cate']))