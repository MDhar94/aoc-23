def day1():

    data = open('input.txt', 'r').read().split('\n')

    data = [[int(y) for y in x if y.isnumeric()] for x in data]

    data = [
        0 if not lst else (lst[0] + lst[-1]) if len(lst) > 1 else lst[0]
        for lst in data
    ]

    return sum(data)

if __name__ == "__main__":

    print(day1())
