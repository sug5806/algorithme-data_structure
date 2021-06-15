if __name__ == "__main__":
    nums = [6, 2, 6, 5, 1, 2]
    nums.sort()

    # # 오름차순으로 정렬하면 짝수번째에 항상 작은수가 온다.
    # for i, n in enumerate(nums):
    #     if i % 2 == 0:
    #         result += n

    # 파이써닉하게 풀이
    result = sum(sorted(nums)[::2])
    print(result)
