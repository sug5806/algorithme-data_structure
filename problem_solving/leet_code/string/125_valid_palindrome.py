# 리스트로 변환해서 풀기
import collections


def isPalindromeUsingList(example) -> bool:
    strings = []

    for char in example:
        if char.isalnum():
            strings.append(char.lower())

    while len(strings) > 1:
        if strings.pop(0) != strings.pop():
            return False

    return True


# 데크로 풀기
def isPalindromeUsingDeque(example) -> bool:
    strs = collections.deque()

    for char in example:
        if char.isalnum():
            strs.append(char)

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


if __name__ == "__main__":
    example_str = "A man, a plan, a canal: Panama"

    print(isPalindromeUsingList(example_str))
