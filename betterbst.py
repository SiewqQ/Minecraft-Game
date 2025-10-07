from __future__ import annotations
from collections.abc import Callable

from typing import Tuple, TypeVar

from algorithms.mergesort import mergesort
from data_structures.node import TreeNode
from data_structures import *

K = TypeVar('K')
I = TypeVar('I')


class BetterBST(BinarySearchTree[K, I]):
    def __init__(self, elements: ArrayList[Tuple[K, I]]) -> None:
        """
        Initialiser for the BetterBST class.
        We assume that the all the elements that will be inserted
        into the tree are contained within the elements ArrayList.

        As such you can assume the length of elements to be non-zero.
        The elements ArrayList will contain tuples of key, item pairs.

        First sort the elements ArrayList and then build a balanced tree from the sorted elements
        using the corresponding methods below.

        Args:
            elements(ArrayList[tuple[K, I]]): The elements to be inserted into the tree.

        Complexity:
            n = number of elements in the input list / the final number of nodes in the tree

            Best Case Complexity: O(n log n)
            Worst Case Complexity: O(n log n)

        Justification:
            The complexity of __init__ method is dominated by the complexity of both __sort_elements method and __build_balanced_tree method which is
            O(n log n).
        """
        super().__init__()
        new_elements: ArrayList[Tuple[K, I]] = self.__sort_elements(elements)
        self.__build_balanced_tree(new_elements)

    def __sort_elements(self, elements: ArrayList[Tuple[K, I]]) -> ArrayList[Tuple[K, I]]:
        """
        Recall one of the drawbacks to using a binary search tree is that it can become unbalanced.
        If we know the elements ahead of time, we can sort them and then build a balanced tree.
        This will help us maintain the O(log n) complexity for searching, inserting, and deleting elements.

        Args:
            elements (ArrayList[Tuple[K, I]]): The elements we wish to sort.

        Returns:
            ArrayList(Tuple[K, I]]) - elements after being sorted.

        Complexity:
            n = the number of elements in the input list

            Best Case Complexity: O(n log n)
            Worst Case Complexity: O(n log n)

        Justification:
            The __sort_elements method uses mergesort, which has a time complexity of O(n log n) in both the best and worst cases.
            This is because mergesort recursively splits the list into halves (log n levels) and merges them in O(n) time per level as it compare each element at every level.
            The key extraction operation involves constant time operation only, ie. O(1) per element.
            """
        return mergesort(elements, lambda x: x[0])

    def __build_balanced_tree(self, elements: ArrayList[Tuple[K, I]]) -> None:
        """
        This method will build a balanced binary search tree from the sorted elements.

        Args:
            elements (ArrayList[Tuple[K, I]]): The elements we wish to use to build our balanced tree.

        Returns:
            None

        Complexity:
            n = number of elements in the input / the final number of nodes in the tree

            Best Case Complexity: O(n log n)
            Worst Case Complexity: O(n log n)

        Justification:
            The complexity of __build_balanced_tree method is dominated by _build_subtree_aux method which has a complexity of O(n log n).
            Both the best and worst case are identical because a balance tree is assumed to always be built.
        """
        self._build_subtree_aux(elements, 0, len(elements) - 1)

    def _build_subtree_aux(self, elements: ArrayList[Tuple[K, I]], start: int, end: int) -> None:
        """
        This is an auxiliary method for _build_balanced_tree method to construct a balanced subtree from inputted elements

        Args:
            elements (ArrayList[Tuple[K, I]]): Sorted list of (key, item) pairs
            start (int): Starting index of current subtree range
            end (int): Ending index of current subtree range

        Returns:
            None

        Complexity:
            n = number of elements in the input / the final number of nodes in the tree

            Best Case Complexity: O(n log n)
            Worst Case Complexity: O(n log n)

        Justification:
            This method builds a balanced BST by recursively selecting the middle element as the root, ensuring O(log n) depth.
            Each insertion invokes BST __setitem__ which takes O(log n) time in a balanced tree, and since there are n insertions,
            the total complexity is O(n log n). The best and worst cases are the same because the tree is always balanced.
        """
        if start > end:
            return

        mid = (start + end) // 2
        key, item = elements[mid]
        self[key] = item

        self._build_subtree_aux(elements, start, mid - 1)
        self._build_subtree_aux(elements, mid + 1, end)


    def filter_keys(self, filter_func1: Callable[[K], bool], filter_func2: Callable[[K], bool]) -> ArrayList[Tuple[K, I]]:
        """
        Filters the keys in the tree based on two criteria.

        Args:
            filter_func1 (callable): A function that takes a value and returns True if the key is more than criteria1.
            filter_func2 (callable): A function that takes a value and returns True if the key is less than criteria2.

        Returns:
            ArrayList[Tuple[K, I]]: An ArrayList of tuples containing Key,Item pairs that match the filter.

        Complexity:
            n = the number of nodes in the tree

            Best Case Complexity: O(log n ∗ (filter_func1+filter_func2))
            Worst Case Complexity: O(n ∗ (filter_func1+filter_func2))

        Justification:
            The complexity of filter_keys method is dominated by _filter_traverse_aux method which has a best complexity of O(log n ∗ (filter_func1+filter_func2))
            and worst complexity of O(n ∗ (filter_func1+filter_func2)). Returning result is just a constant time operation.
        """
        result = ArrayList(len(self))
        self._filter_traverse_aux(self.root, filter_func1, filter_func2, result)
        return result

    def _filter_traverse_aux(self, current: TreeNode[K, I], filter_func1: Callable[[K], bool], filter_func2: Callable[[K], bool], result: ArrayList[Tuple[K, I]]) -> None:
        """
        Helper method that performs an optimized in-order traversal, skipping subtrees when possible based on filter conditions.

        Args:
            current (TreeNode[K, I]): Current subtree node
            filter_func1 (callable): A function that takes a value and returns True if the key is more than criteria1.
            filter_func2 (callable): A function that takes a value and returns True if the key is less than criteria2.
            result (ArrayList[Tuple[K, I]]): An ArrayList of tuples containing Key,Item pairs that match the filter.

        Returns:
            None

        Complexity:
            n = the number of nodes in the tree

            Best Case Complexity: O(log n ∗ (filter_func1+filter_func2))
            Worst Case Complexity: O(n ∗ (filter_func1+filter_func2))

        Justification:
            The best case arises when the filter range is narrow and only overlaps with a small portion of the tree.
            For example, when criteria1 is just above the root key, and criteria2 is larger than the largest key or vice versa.
            In such cases, the if statement of filter functions evaluate to False, allowing the traversal to skip entire left subtrees and only follow a single path from root to leaf.
            For a balanced tree, a single path has a height of O(log n), so only O(log n) nodes are visited, with each node requiring constant-time evaluation of the two filter functions.
            Therefore, the best-case time complexity is O(log n ∗ (filter_func1+filter_func2)).

            The worst case occurs when the filter range is so broad that it includes nearly all the keys in the tree—for example,
            if criteria1 is smaller than the smallest key AND criteria2 is larger than the largest key.
            In this situation, both filter_func1(current.key) and filter_func2(current.key) will evaluate to True for most nodes,
            causing the traversal to visit both left and right subtrees recursively for nearly every node.
            As a result, all n nodes may be visited, and since each node involves evaluating both filter functions (each costing T_f1 and T_f2, respectively),
            the total time complexity becomes O(n ∗ (filter_func1+filter_func2)), regardless of whether the tree is balanced.
        """
        if current is None:
            return

        # check if we need to explore left subtree, if current key > lower_bound/criteria1 (filter_func1), then traverse left as left might have smaller keys
        if filter_func1(current.key):
            self._filter_traverse_aux(current.left, filter_func1, filter_func2, result)

        # check current node to decide whether to add current node's item to the result
        if filter_func1(current.key) and filter_func2(current.key):
            result.append((current.key, current.item))

        # check if we need to explore right subtree, if current key < upper_bound/criteria2 (filter_func2), then traverse right as right might have larger keys
        if filter_func2(current.key):
            self._filter_traverse_aux(current.right, filter_func1, filter_func2, result)

