import random

import node_management

if __name__ == "__main__":
    bst_nums = set()

    while len(bst_nums) != 100:
        bst_nums.add(random.randint(0, 999))

    print(bst_nums)

    head = node_management.Node(500)
    binary_tree = node_management.NodeManagement(head)

    for number in bst_nums:
        binary_tree.insert(number)

    # 검색 기능 확인
    for number in bst_nums:
        if binary_tree.search(number) is False:
            print("search failed : ", number)

    delete_nums = set()
    bst_nums = list(bst_nums)
    while len(delete_nums) != 10:
        delete_nums.add(bst_nums[random.randint(0, 99)])

    # 삭제 기능 확인
    for del_num in delete_nums:
        if binary_tree.delete(del_num) is False:
            print('delete failed', del_num)
