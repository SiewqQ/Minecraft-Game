from __future__ import annotations
from typing import Iterable

from data_structures import *
from minecraft_block import MinecraftBlock


class Miner:
    """
    A class representing a miner in a mining simulation.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes the miner with a name and an empty inventory.

        Args:
            name (str): The name of the miner.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

        Justification:
            Assigning name to self.name is a constant time operation. Creating an empty LinkedList is also a constant-time operation.
            Thus, the best and worst case are the same as only constant time operation, O(1) is involved.
        """
        self.name = name
        self.inventory = LinkedList()

    def mine(self, block: MinecraftBlock) -> None:
        """
        Mines a block and adds the item to the miner's bag.

        Args:
            block (MinecraftBlock): The block to be mined.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

        Justification:
            Appending the item to the end of the linked list is O(1) as we have a reference to the rear of the list.
        """
        self.inventory.append(block.item)

    def clear_inventory(self) -> Iterable:
        """
        Clears the miner's inventory and returns what he had in the inventory before the clear.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

        Justification:
            This method performs constant time operations as it only requires to assign the reference of the current self.inventory to a variable 'old inventory',
            then create a new empty LinkedList to assign its reference to self.inventory. The status of self.inventory is then updated with a new empty LinkedList.
        """
        old_inventory = self.inventory
        self.inventory = LinkedList()  # replace with a new, empty LinkedList
        return old_inventory
