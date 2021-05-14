class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeManagement:
    def __init__(self, root):
        self.root = root

    def get_value(self):
        return self.root.value

    def insert(self, value):
        self.current_node = self.root
        while True:
            if value < self.current_node.value:
                if self.current_node.left is not None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right is not None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.root

        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right

        return False

    def delete(self, value):
        # 삭제할 노드 탐색
        searched = False
        self.current_node = self.root
        self.parent = self.root
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        # 삭제할 노드가 없음
        if searched is False:
            return False

        # 삭제할 노드를 찾음
        # 1. 삭제할 노드가 리프노드 경우
        if self.current_node.left is None and self.current_node.right is None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None

        # 2. 삭제할 노드가 Child Node를 가지고 있을 경우
        # 2-1 Child Node가 삭제할 노드의 왼쪽에 있을 경우
        elif self.current_node.left is not None and self.current_node.right is None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left

        # 2-2 Child Node가 삭제할 노드의 오른쪽에 있을 경우
        elif self.current_node.left is None and self.current_node.right is not None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # 3. 삭제할 노드가 Child Node를 양쪽 모두 가지고 있을 경우
        elif self.current_node.left is not None and self.current_node.right is not None:
            # 3-1 삭제할 Node가 Parent Node 왼쪽에 있는 경우
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                self.change_node_parent.left = None
                if self.change_node.right:
                    self.change_node_parent.right = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.change_node.left

            # 3-2 삭제할 Node가 Parent Node 오른쪽에 있는 경우
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left

        return True
