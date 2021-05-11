import random


def quick_sort(list_data):
    if len(list_data) <= 1:
        return list_data

    pivot = list_data[len(list_data) // 2]

    left = [item for item in list_data if pivot > item]
    print(left)

    right = [item for item in list_data if pivot < item]
    print(right)
    print()

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    data = random.sample(range(10), 5)

    print(data)
    print()
    print(quick_sort(data))
