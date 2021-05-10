import random

if __name__ == '__main__':
    data = random.sample(range(100), 50)

    print(data)

    for i in range(len(data) - 1):
        swap = False
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swap = True

        if not swap:
            break

    print(data)
