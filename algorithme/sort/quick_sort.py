import random


def quick_sort(list_data):
    if len(list_data) <= 1:
        return list_data

    pivot = list_data[len(list_data) // 2]

    left = [item for item in list_data if pivot > item]

    right = [item for item in list_data if pivot < item]

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    data = random.sample(range(1000), 30)

    print("정렬 전 : ", data)
    print()
    print("정렬 후 : ", quick_sort(data))
