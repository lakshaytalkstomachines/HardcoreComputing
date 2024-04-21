"""
Basic Implementation of a tree.
"""

from typing import Optional


class Node:
    """
    This defines a unit of data (integer).
    """

    def __init__(self, data: Optional[int] = None) -> None:
        """
        Initializes data.
        """
        self.data = data

    def __str__(self) -> str:
        return f"Node({'--' if not self.data else self.data})"


def main():
    """
    Main Runner
    """
    nodeList = []
    for i in range(20):
        nodeList.append(Node(i))

    for node in nodeList:
        print(node)

    # Special Node with no Data.
    print(Node())


if __name__ == "__main__":
    main()
