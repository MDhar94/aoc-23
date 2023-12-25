def day1_part1():

    data = open('input.txt', 'r').read().split('\n')

    data = [[y for y in x if y.isnumeric()] for x in data]

    data = [
        0 if not lst else (int(lst[0] + lst[-1])) if len(lst) > 1 else int(lst[0] + lst[0])
        for lst in data
    ]

    return sum(data)

if __name__ == "__main__":

    print(day1_part1())
