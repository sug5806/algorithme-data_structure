# 간단한 해쉬 함수를 만들기 (나무기를 통해 나머지 값을 사용하기)
def custom_hash_func(key):
    return key % 5


def storage_data(data, value):
    key = ord(data[0])
    hash_address = custom_hash_func(key)
    hash_table[hash_address] = value


def get_value(data):
    key = ord(data[0])
    hash_address = custom_hash_func(key)
    return hash_table[hash_address]


if __name__ == '__main__':
    hash_table = list([0 for i in range(10)])

    storage_data('Andy', '01012341234')
    storage_data('Dave', '01033332222')
    storage_data('Trump', '01055556666')

    print(hash_table)
    print(get_value('Andy'))
