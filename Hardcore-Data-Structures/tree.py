"""
Basic Implementation of a tree.
"""


class Node:
    """
    This defines a unit of data (integer).
    """

    def __init__(self, data: int) -> None:
        """
        Initializes data.
        """
        self.data = data

    def __str__(self) -> str:
        return f"Node({self.data})"


def main():
    """
    Main Runner
    """
    nodeList = []
    for i in range(20):
        nodeList.append(Node(i))

    for node in nodeList:
        print(node)


if __name__ == "__main__":
    main()
