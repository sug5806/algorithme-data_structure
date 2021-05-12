import random


def split(list_data):
    if len(list_data) < 1:
        return list_data

    mid_index = len(list_data) // 2

    left_list = split(list_data[:mid_index])
    right_list = split(list_data[mid_index:])

    return merge(left_list, right_list)


def merge(left_list, right_list):
    left_start_index, right_start_index = 0, 0
    temp_list = list()

    while len(left_list) > left_start_index and len(right_list) > right_start_index:

        if left_list[left_start_index] < right_list[right_start_index]:
            temp_list.append(left_list[left_start_index])
            left_start_index += 1

        else:
            temp_list.append(right_list[right_start_index])
            right_start_index += 1

    while len(left_list) > left_start_index:
        temp_list.append(left_list[left_start_index])
        left_start_index += 1

    while len(right_list) > right_start_index:
        temp_list.append(right_list[right_start_index])
        right_start_index += 1

    return temp_list


def merge_sort(list_data):
    return split(list_data)


if __name__ == '__main__':
    data = random.sample(range(1000), 15)

    print(data)

    print(merge_sort(data))
