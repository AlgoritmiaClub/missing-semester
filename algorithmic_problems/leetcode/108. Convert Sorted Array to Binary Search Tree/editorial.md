# [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/)


### Recursive Divide and Conquer

The most common approach is to apply **divide and conquer**:

1. Pick the **middle element** of the array as the root.
2. Recursively build the left subtree from the left half of the array.
3. Recursively build the right subtree from the right half of the array.
4. Stop recursion when the subarray becomes empty.

This ensures the tree is height-balanced.

- **Time Complexity:** $O(n)$ (each element is visited once)
- **Space Complexity:** $O(\log n)$ (recursion stack depth for balanced tree)

Example for input `[-10, -3, 0, 5, 9]`:

    0
   / \
-10   5
  \     \
  -3      9

---

# Iterative with Queue (BFS-style) — no placeholders

This builds a height-balanced BST iteratively using a queue that stores tuples `(parent, l, r, is_left)`.  
Each `TreeNode` is created **only when its value is known** (no placeholder nodes).

1. If `nums` is empty, return `None`.  
2. Compute the initial middle index `mid = (0 + n - 1) // 2` and create the root `root = TreeNode(nums[mid])`.  
3. Initialize a queue (`collections.deque`) and enqueue the left subrange `(root, 0, mid-1, True)` and the right subrange `(root, mid+1, n-1, False)` if they exist.  
4. While the queue is not empty:  
   - Dequeue `(parent, l, r, is_left)`.  
   - Compute `m = (l + r) // 2` and create `node = TreeNode(nums[m])`.  
   - Attach `node` to `parent.left` if `is_left` is `True`, otherwise to `parent.right`.  
   - If valid, enqueue the subranges `(node, l, m-1, True)` and `(node, m+1, r, False)`.  
5. When done, return `root`.

- **Time:** `O(n)` — each element is turned into a node exactly once.  
- **Space:** `O(n)` in the worst case for the queue / tree structure.