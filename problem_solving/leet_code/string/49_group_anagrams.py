import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagram = collections.defaultdict(list)

    for word in strs:
        anagram[''.join(sorted(word))].append(word)

    return list(anagram.values())


if __name__ == "__main__":
    example = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(example))
