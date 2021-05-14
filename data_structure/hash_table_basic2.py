def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value


def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]


if __name__ == '__main__':
    hash_table = list([0 for i in range(8)])

    save_data('Dave', '01020202020')
    save_data('Andy', '01050505050')

    print(read_data('Dave'))
    print(hash_table)
