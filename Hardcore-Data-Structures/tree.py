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
        """
        String representation of node. Helps in printing.
        """
        return f"Node({'--' if self.data is None else self.data})"

    def return_memory_id(self, hex_mode=False) -> int:
        """
        this method prints the memory id.

        args:
            hex_mode: If true would return hex value of memory address otherwise int.
        """
        memory_id = id(self)

        return hex(memory_id) if hex_mode else memory_id


def main():
    """
    Main Runner
    """
    nodeList = []
    for i in range(20):
        nodeList.append(Node(i))

    for node in nodeList:
        print(node.print_memory_id(hex_mode=True), end="  |  ")
        print(node)
    # Special Node with no Data.
    print(Node())


if __name__ == "__main__":
    main()
