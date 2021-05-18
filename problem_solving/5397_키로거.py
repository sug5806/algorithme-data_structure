if __name__ == "__main__":
    count = int(input())

    for _ in range(count):
        stack1 = []
        stack2 = []
        test_case = input()

        for char in test_case:
            if char == '<':
                if stack1:
                    stack2.append(stack1.pop())
            elif char == '>':
                if stack2:
                    stack1.append(stack2.pop())
            elif char == '-':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(char)

        stack1.extend(reversed(stack2))
        print(''.join(stack1))
