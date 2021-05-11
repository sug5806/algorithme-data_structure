import random

if __name__ == '__main__':
    data = random.sample(range(100), 50)

    print(data)

    for stand in range(len(data) - 1):
        # print(stand)
        min_value_index = stand
        for index in range(stand + 1, len(data)):
            if data[min_value_index] > data[index]:
                min_value_index = index

        data[stand], data[min_value_index] = data[min_value_index], data[stand]

    print(data)
