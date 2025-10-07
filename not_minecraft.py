from __future__ import annotations

from algorithms.mergesort import mergesort
from cave_system import CaveSystem
from data_structures import *
from minecraft_block import MinecraftBlock
from minecraft_checklist import MinecraftChecklist
from miner import Miner
from random_gen import RandomGen


class NotMinecraft:
    """
    A class representing a NotMinecraft game.
    """

    def __init__(self, cave_system: CaveSystem, checklist: MinecraftChecklist) -> None:
        """
        Initializes the NotMinecraft game.
        Args:
            cave_system (CaveSystem): The cave system for the game.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

        Justification:
            Assigning values and initializing a Miner object with name "Steve" requires constant time operations only, thus O(1).
        """
        self.miner = Miner("Steve")
        self.cave_system = cave_system
        self.checklist = checklist

    def dfs_explore_cave(self) -> ArrayList[MinecraftBlock]:
        """
        Performs a depth-first search (DFS) to explore the cave system and collect blocks.
        Returns:
            ArrayList[MinecraftBlock]: A list of collected blocks.
        Complexity:
            Not required
        """
        visited = LinearProbeTable()
        blocks_found = ArrayList()
        stack = LinkedStack()

        stack.push(self.cave_system.entrance)  # start DFS from entrance

        while not stack.is_empty():
            current_node = stack.pop()

            # only process node if it hasn't been visited
            if current_node.name not in visited:
                visited[current_node.name] = True

                # add all blocks from current node to list of found blocks
                for i in range(len(current_node.blocks)):
                    blocks_found.append(current_node.blocks[i])

                # add unvisited neighbours to the stack in reverse order so node.neighbours[0] will be on top of the stack and explored next
                for i in range(len(current_node.neighbours) - 1, -1, -1):
                    neighbor = current_node.neighbours[i]

                    # only push to stack if the neighbor hasn't been visited yet
                    if neighbor.name not in visited:
                        stack.push(neighbor)

        return blocks_found

    def objective_mining_filter(self, blocks: ArrayList[MinecraftBlock], block1: MinecraftBlock,
                                block2: MinecraftBlock) -> ArrayList:
        """
        Given a list of blocks, filter the blocks that should be considered according to scenario 1.

        Args:
            blocks (ArrayList[MinecraftBlock]): The list of blocks to mine.
            block1 (MinecraftBlock): Filtered blocks should have a ratio of value to mining time > block1.
            block2 (MinecraftBlock): Filtered blocks should have a ratio of value to mining time < block2.

        Complexity:
            n = number of inputted blocks discovered while exploring the cave
            m = number of blocks in checklist
            f = number of filtered blocks from checklist

            Best Case Complexity: O(log m + n * f)
            Worst Case Complexity: O (m + n * f)

        Justification:
            Best case happens during the best case of get_optimal_blocks method too, ie. O(log m) which is dominated by filter_keys method too
            when the computed ratio bounds (lower and upper) define a narrow range and only overlaps with a small portion of the tree.
            This causes filter_keys method to skip entire subtrees and only follow a single path from root to leaf that traverse nodes at log m levels.
            The for loop iterates discovered inputted blocks with a time complexity of O(n),
            The 'if' statement checks if the discovered block is in the filtered blocks from checklist with a complexity of O(f)
            Thus, the overall best case is O(log m) + O(n) * O(f) = O(log m + n * f)

            Worst case happens during the worst case of get_optimal_blocks method too, ie. O(m) which is dominated by filter_keys method too
            when the ratio bounds cover a wide range that includes all or most of the keys in the BST, requiring the filter operation to traverse the entire tree.
            In this case, the filter functions are applied to each node, making the filter step cost O(m) as it needs to traverse all the nodes.
            The for loop iterates discovered inputted blocks with a time complexity of O(n),
            The 'if' statement checks if the discovered block is in the filtered blocks from checklist with a complexity of O(f)
            Thus, the overall worst case is O(m) + O(n) * O(f) = O(m + n * f)
        """
        # get optimal blocks from checklist that is between the threshold of block 1 and block 2
        optimal_blocks = self.checklist.get_optimal_blocks(block1, block2)

        result = ArrayList(len(optimal_blocks))

        # filter input blocks by going through all the existing blocks
        for block in blocks:
            # only include blocks that are in checklist of miner and fulfill the threshold of block 1 and block 2 (stored in optimal_table)
            if block in optimal_blocks:
                result.append(block)

        return result

    def objective_mining(self, blocks: ArrayList[MinecraftBlock]) -> None:
        """
        Mines the cave system to achieve the objective of collecting blocks.\

        Args:
            blocks (ArrayList[MinecraftBlock]): The list of blocks to mine.

        Complexity:
            n = the number of elements in the input list

            Best Case Complexity: O(n log n)
            Worst Case Complexity: O(n log n)

        Justification:
            The object_mining method uses mergesort, which has a time complexity of O(n log n) in both the best and worst cases.
            This is because mergesort recursively splits the list into halves (log n levels) and merges them in O(n) time per level.
            The key's operation of getting ratio involves constant time operation only, ie. O(1) per element.
            Iterating over sorted blocks has a time complexity of O(n). The mine method has constant time operation of O(1), thus the overall complexity for this method is
            dominated by the complexity of merge sort, ie. O(n log n).

        """
        # Sort blocks by ratio in descending order using merge sort
        sorted_blocks = mergesort(blocks, lambda x: -x.ratio())  # Negative for descending order

        # Mine blocks in sorted order
        for block in sorted_blocks:
            self.miner.mine(block)

    def objective_mining_summary(self, blocks: ArrayList[MinecraftBlock], block1: MinecraftBlock,
                                 block2: MinecraftBlock) -> None:
        """
        Returns the summary of the objective mining.
        This is to explain how objective mining will be called and tested.
        Complexity:
            Not Required
        """
        filtered_blocks = self.objective_mining_filter(blocks, block1, block2)

        self.chicken_jockey_attack(filtered_blocks)

        self.objective_mining(filtered_blocks)

    def profit_mining(self, blocks: ArrayList[MinecraftBlock], time_in_seconds: int) -> None:
        """
        Mines the cave system casually.
        Args:
            blocks (ArrayList[MinecraftBlock]): The list of blocks to mine.
            time_in_seconds (int): The time in seconds to mine.

        Complexity:
            n = the number of blocks

            Best Case Complexity: O(n)
            Worst Case Complexity: O(n log n)

        Justification:
            The heapify method has a complexity of O(n). Assigning variable name is a constant time operation, O(1).
            The while loop will iterate n times as there are n elements.
            Best case of get_max method is O(1) when each of all the rightmost element at the last level of heap moved to the root satisfy the heap property
            ie. the key at the root is larger than the children key. Thus, the new root node doesn't need to sink.
            Therefore, the complexity of this method is dominated by the while loop to remove n elements from the block heap, ie. O(n) * O(1) = O(n).

            The heapify method as a complexity of O(n). Assigning variable name is a constant time operation, O(1).
            The while loop will iterate n times as there are n elements.
            Worst case of get_max is O(log n) when each of all the rightmost element at the last level of heap moved to the root does not satisfy the heap property
            ie. the key at the root is larger than the children key. Thus, the new root node needs to sink to reach the correct position that satisfy the heap property,
            which has a time operation of O(log n).
            Therefore, the complexity of this method is dominated by the while loop to remove n elements from the block heap, ie. O(n) * O(log n) = O(n log n).
        """
        # max-heap based on the value-to-time ratio
        block_heap = MaxHeap.heapify(blocks, len(blocks))

        # mine blocks in the order of priority until time runs out
        remaining_time = time_in_seconds

        while remaining_time > 0 and len(block_heap) > 0:
            # get the most profitable block
            block = block_heap.get_max()

            if block.hardness <= remaining_time:
                self.miner.mine(block)
                remaining_time -= block.hardness

                if remaining_time == 0:
                    break  # not enough time for this block

    def chicken_jockey_attack(self, blocks: ArrayList[MinecraftBlock]) -> None:
        """
        Chicken Jockey Attack
        Args:
            blocks (ArrayList[MinecraftBlock]): The list of blocks to mine.
        Complexity:
            Not required
        """
        RandomGen.random_shuffle(blocks)

    def main(self, scenario: int, **criteriaArgs) -> None:
        """
        Main function to run the NotMinecraft game.
        Args:
            scenario (int): The scenario number to run.
            criteriaArgs (dict): Additional arguments for the scenario.
        Complexity:
            Not required
        Sample Usage:
            not_minecraft = NotMinecraft(cave_system, checklist)
            not_minecraft.main(1, block1=block1, block2=block2)
            not_minecraft.main(2, time_in_seconds=60)
        """
        if scenario == 1:
            blocks = self.dfs_explore_cave()
            self.objective_mining_summary(blocks, **criteriaArgs)
        elif scenario == 2:
            blocks = self.dfs_explore_cave()
            self.profit_mining(blocks, **criteriaArgs)
