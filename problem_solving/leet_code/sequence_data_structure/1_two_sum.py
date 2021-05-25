from typing import List

# 두 수의 합이 target이 되는 인덱스 반환하기
def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}

    # 키와 값을 바꿔서 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    print(nums_map)

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 13

    print(twoSum(nums, target))
