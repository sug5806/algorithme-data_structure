import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    values = collections.deque()

    while head is not None:
        values.append(head.val)
        head = head.next

    while len(values) > 1:
        if values.popleft() != values.pop():
            return False

    return True


if __name__ == "__main__":
    head = ListNode(1, None)
    head.next = ListNode(2, None)
    head.next.next = ListNode(2, None)
    head.next.next.next = ListNode(1, None)

    palindrome = isPalindrome(head)
    print(palindrome)
