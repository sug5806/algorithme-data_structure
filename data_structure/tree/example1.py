import node
import node_management

if __name__ == "__main__":
    head = node.Node(1)
    BST = node_management.NodeManagement(head)
    BST.insert(2)
    BST.insert(3)
    BST.insert(4)
    BST.insert(9)
    BST.insert(1)

    print(BST.search(1))
