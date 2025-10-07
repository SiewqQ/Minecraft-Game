from __future__ import annotations


class MinecraftItem:
    """
    A class representing an item with a name, description, and rarity.
    """

    def __init__(self, name: str, description: str, value: int) -> None:
        """
        Initializes an Item instance with a name, description, and rarity.

        Args:
            name (str): The name of the item.
            description (str): A description of the item.
            value (int): The value of the item.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        self.name = name
        self.description = description
        self.value = value

    def __eq__(self, other: 'MinecraftItem') -> bool:
        """
        Checks if two items are equal based on their name.

        Args:
            other (MinecraftItem): The other item to compare.

        Returns:
            bool: True if the items are equal, False otherwise.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        return self.name == other.name

    def __str__(self) -> str:
        """
        Returns a string representation of the item.

        Returns:
            str: A string representation of the item.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        return f"Item(name={self.name}, description={self.description}, value={self.value})"

    def __repr__(self) -> str:
        """
        Returns a string representation of the item for debugging.

        Returns:
            str: A string representation of the item.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        return str(self)


class MinecraftBlock:
    """
    A class representing a block in Minecraft containing an item.
    """

    def __init__(self, name: str, description: str, hardness: int, item: MinecraftItem) -> None:
        """
        Initializes a MinecraftBlock instance with a name, description, hardness, int.

        Args:
            name (str): The name of the block.
            description (str): A description of the block.
            hardness (int): The hardness of the block.
            item (MinecraftItem): The item contained in the block.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        self.name = name
        self.description = description
        self.hardness = hardness
        self.item = item

    def ratio(self) -> float:
        """
        Returns the value-to-hardness ratio for the block.

        Args:
            None

        Returns:
            float: the ratio of a minecraft block

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

        Justification:
            Both the best and worst case are the same because it only involves constant time operations of accessing item's value and
            performing division operation to obtain the ratio of a block.
        """

        return self.item.value / self.hardness

    def __eq__(self, other: 'MinecraftBlock') -> bool:
        """
        Compares two MinecraftBlock instances.

        Args:
            other (MinecraftBlock): The other block to compare with.

        Returns:
            bool: True if this block is equal to the other block, False otherwise.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

        Justification:
            The comparison is based on the name of the block.
            This is a constant time operation as it involves simple arithmetic and comparison.
        """

        return self.name == other.name

    def __lt__(self, other: 'MinecraftBlock') -> bool:
        """
        Checks if this block's value-to-hardness ratio is less than another block's.

        Args:
            other (MinecraftBlock): The other block to compare with.

        Returns:
            bool: True if self's ratio is less than other's ratio, False otherwise.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

        Justification:
            The best and worse case are the same as this method only involves constant time operation of comparison. The ratio() method has a constant time complexity of O(1) too.
        """
        return self.ratio() < other.ratio()

    def __le__(self, other: 'MinecraftBlock') -> bool:
        """
        Checks if this block's value-to-hardness ratio is less than or equal to another block's.

        Args:
            other (MinecraftBlock): The other block to compare with.

        Returns:
            bool: True if self's ratio is less than or equal to other's ratio, False otherwise.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

        Justification:
            The best and worse case are the same as this method only involves constant time operation of comparison. The ratio() method has a constant time complexity of O(1) too.
        """
        return self.ratio() <= other.ratio()

    def __gt__(self, other: 'MinecraftBlock') -> bool:
        """
        Checks if this block's value-to-hardness ratio is greater than another block's.

        Args:
            other (MinecraftBlock): The other block to compare with.

        Returns:
            bool: True if self's ratio is greater than other's ratio, False otherwise.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

        Justification:
            The best and worse case are the same as this method only involves constant time operation of comparison. The ratio() method has a constant time complexity of O(1) too.
        """
        return self.ratio() > other.ratio()

    def __ge__(self, other: 'MinecraftBlock') -> bool:
        """
        Checks if this block's value-to-hardness ratio is greater than or equal to another block's.

        Args:
            other (MinecraftBlock): The other block to compare with.

        Returns:
            bool: True if self's ratio is greater than or equal to other's ratio, False otherwise.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

        Justification:
           The best and worse case are the same as this method only involves constant time operation of comparison. The ratio() method has a constant time complexity of O(1) too.
        """
        return self.ratio() >= other.ratio()

    def __str__(self) -> str:
        """
        Returns a string representation of the block.

        Returns:
            str: A string representation of the block.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        return f"Block(name={self.name}, description={self.description}, hardness={self.hardness}, item={self.item})"

    def __repr__(self) -> str:
        return str(self)
