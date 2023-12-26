def day1_part1(data):

    data = [[y for y in x if y.isnumeric()] for x in data]

    data = [
        0 if not lst else (int(lst[0] + lst[-1])) if len(lst) > 1 else int(lst[0] + lst[0])
        for lst in data
    ]

    return data

def day1_part2(data):

    num_dict = {"one": "o1e"
                , "two": "t2o"
                , "three": "t3e"
                , "four": "f4r"
                , "five": "f5e"
                , "six":"s6x"
                , "seven": "s7n"
                , "eight": "e8t"
                , "nine": "n9e"}

    data_clean = []

    for line in data:
        for key, value in num_dict.items():
            line = line.replace(key, value)
        data_clean.append(line)

    calibrations = day1_part1(data_clean)

    return calibrations

if __name__ == "__main__":

    data = open('input.txt', 'r').read().split('\n')

    part1 = sum(day1_part1(data))

    part2 = sum(day1_part2(data))

    print(part1, part2)
