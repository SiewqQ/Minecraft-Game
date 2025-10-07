from __future__ import annotations

from betterbst import BetterBST
from data_structures import *
from minecraft_block import MinecraftBlock, MinecraftItem


class MinecraftChecklist:
    def __init__(self, blocks: ArrayR[MinecraftBlock]) -> None:
        """
        Initializes the MinecraftChecklist instance with a list of blocks.

        Complexity:
            n = number of given blocks

            Best Case Complexity: O(n log n)
            Worst Case Complexity: O(n log n)

        Justification:
            Initializing an ArrayList takes O(n) time. Iterating through all the inputted blocks takes O(n) time to be appended into ArrayList.
            The complexity of __init__ method is dominated by the initialization of self.checklist with BetterBST, which has a complexity of O(n log n).
        """
        elements = ArrayList(len(blocks))

        for block in blocks:
            elements.append((block.ratio(), block))

        self.checklist = BetterBST(elements)

    def __contains__(self, item: MinecraftBlock) -> bool:
        """
        Checks if the item is in the checklist.

        Complexity:
            n = number of blocks in the checklist

            Best Case Complexity: O(1)
            Worst Case Complexity: O(log n)

        Justification:
            The best case occurs when the ratio (key) of the inputted item corresponds to the key of the root node of BetterBST.
            Thus, the overall complexity is O(1) as it doesn't need to traverse down the tree.

            The worst case happens when the inputted item is found at a leaf node in the balanced BetterBST or the item is not present in the BetterBST.
            Searching in a balanced BST of n items takes O(log n) time if the node we are finding for is the leaf node
            as it involves traversing a single path from the root to the leaf of log n levels (or a point where a leaf would be). Thus, O(log n).
        """
        key = item.ratio()

        try:
            # checking if the item is in BST or not by using the item's ratio as key to store item
            return self.checklist[key] == item

        except KeyError:
            # if item is not in BST
            return False

    def __len__(self) -> int:
        """
        Returns the number of blocks in the checklist.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

        Justification:
            Both the best and worst case complexity are the same as accessing len requires constant time operation only.
        """
        return len(self.checklist)

    def add_block(self, block: MinecraftBlock) -> None:
        """
        Adds a block to the checklist.

        Complexity:
            n = the number of blocks in the checklist.

            Best Case Complexity: O(log n)
            Worst Case Complexity: O(log n)

        Justification:
            Obtaining the key of BST using block.ratio() is an O(1) operation.
            Checking if the key is absent in the balanced BST self.checklist before adding takes O(log n) for a balanced tree, as it requires to traverse log n levels of tree nodes.
            If there is no node with the same key is present, then only the key will be inserted into the tree node. Thus, O(log n) for both best and worst case.
        """
        key = block.ratio()

        # check if key exist in checklist first as every block has a unique name and unique ratio, else don't need to add existing block to checklist
        if key not in self.checklist:
            self.checklist[key] = block

    def remove_block(self, block: MinecraftBlock) -> None:
        """
        Removes a block from the checklist.

        Complexity:
            n = the number of blocks in the checklist.

            Best Case Complexity: O(log n)
            Worst Case Complexity: O(log n)

        Justification:
            Best case of remove_block method is when the block we want to remove is at the leaf node where it is not required to search for the successor of that node.
            However, reaching the leaf node requires to traverse nodes at log n levels, which has a complexity of O(log n).

            Worst case of remove_block method is when the block we want to remove is the root node where we need to search for the successor of the node.
            This requires traversing nodes at log n levels to search for the successor node, which has a complexity of O(log n) too.
        """
        key = block.ratio()

        if key in self.checklist:
            del self.checklist[key]

    def get_sorted_blocks(self) -> ArrayR[MinecraftBlock]:
        """
        Returns the sorted blocks in the checklist.

        Complexity:
            n = the number of blocks in the checklist.

            Best Case Complexity: O(n)
            Worst Case Complexity: O(n)

        Justification:
            Allocating memory for an arrayR of size n takes O(n) time. Initializing index = 0 is O(1) constant time operation.
            Iterating all the blocks in the checklist requires a time complexity of O(n), where for each block, accessing the index and assigning the block to ArrayR are constant time operations.
            Thus, the complexity of the iteration and allocation memory for ArrayR dominates this method, ie. O(n).
        """
        result = ArrayR(len(self))

        index = 0

        #iterate BST using in order traversal to get sorted blocks in ascending order
        for block in self.checklist:
            result[index] = block.item
            index += 1

        return result

    def get_optimal_blocks(self, block1: MinecraftBlock, block2: MinecraftBlock) -> ArrayR[MinecraftBlock]:
        """
        Returns the optimal blocks between two given blocks.
        Criteria 1:
            - Optimal blocks have a ratio of value to mining time more than the same ratio for block1.
        Criteria 2:
            - Optimal blocks have a ratio of value to mining time less than the same ratio for block2.

        Args:
            block1 (MinecraftBlock): The first block.
            block2 (MinecraftBlock): The second block.

        Returns:
            ArrayR: An array of optimal blocks between the two given blocks.

        Complexity:
            n =  the number of total blocks.

            Best Case Complexity: O(log n)
            Worst Case Complexity: O(n)

        Justification:
            Best case happens during the best case of filter_keys method too when the computed ratio bounds (lower and upper) define a narrow range and only overlaps with a small portion of the tree.
            For example, when criteria1 ratio is just above the root key, and criteria2 ratio is larger than the largest key or vice versa.
            This causes filter_keys method to skip entire subtrees and only follow a single path from root to leaf that traverse nodes at log n levels.
            Since the filter function calls are O(1) and the tree traversal touches only a logarithmic number of nodes, the filter step takes O(log n).
            Then, allocating an ArrayR of size M to store filtered blocks has a complexity of O(m). Iterating the filtered items to copy into ArrayR takes O(m) too.
            Since we know that m is always smaller than n as filtered blocks will be lesser than total blocks, the complexity of O(log n), ie. the complexity of filter_keys method dominates the complexity of O(m).
            Therefore, the total cost remains O(log n).

            Worst case occurs during the worst case of filter_keys method too when the ratio bounds cover a wide range that includes all or most of the keys in the BST, requiring the filter operation to traverse the entire tree.
            In this case, the filter functions are applied to each node, making the complexity of filter step to be O(n) as it needs to traverse all the nodes.
            Furthermore, if all or most of the blocks satisfy the filter criteria, then we can say m is approximately equal to n or still smaller than n.
            Thus, allocating the result ArrayR of size m and copying each of the m filtered blocks into it both take approximately O(n) time too.
            Therefore, the overall complexity is dominated by the complexity of filter_keys method, ie. O(n), since m is always smaller than n / m approximately equals to n.
        """
        #determining lower and upper bound to obtain the range
        lower = min(block1.ratio(), block2.ratio())
        upper = max(block1.ratio(), block2.ratio())

        def filter_func1(k):
            return k > lower

        def filter_func2(k):
            return k < upper

        # filtered is an ArrayList of (key, block) tuples sorted by key
        filtered = self.checklist.filter_keys(filter_func1, filter_func2)

        # copying optimal blocks from filtered to ArrayR
        result = ArrayR(len(filtered))
        i = 0
        for _, block in filtered:
            result[i] = block
            i += 1
        return result
