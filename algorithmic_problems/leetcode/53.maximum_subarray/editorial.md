# [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

**Problem.** Given an integer array `nums`, find a contiguous subarray with the
largest sum and return that sum.

## Building up intuition

We start from the simplest baselines to understand the structure of the answer.

**Brute force (enumeration).**\
Enumerate all subarrays and compute their sums. The naïve triple loop that
recomputes each sum is $O(n^3)$ and serves only as a teaching baseline.\
A practical brute-force improves this by keeping a running sum while extending
the right end, giving $O(n^2)$ time and $O(1)$ extra space. Despite being
clearer, this still times out for large $n$.

**From $O(n^2)$ to $O(1)$ extra space and $O(n)$ time.**\
The key observation is that only the **best subarray ending at each index**
matters for future extensions. If the best subarray ending at $i-1$ is negative,
carrying it forward can only hurt the sum at $i$, so we should drop it and start
fresh at $i$. This greedy idea yields a one-pass linear solution (Kadane).

## Kadane’s algorithm (linear time, constant space)

Maintain two values while scanning left to right:

- `cur`: the maximum sum of a subarray that **must end** at the current
  position.
- `best`: the maximum sum seen anywhere so far.

For each $x \in nums$, decide whether to **extend** the previous subarray or
**start** at $x$: $$
cur = \max(x,\ cur + x), \qquad best = \max(best,\ cur).
$$

**Correctness (invariant).**\
At index $i$, $cur$ equals the maximum sum of any subarray that ends at $i$. If
the previous $cur$ was negative, replacing it with $x$ cannot make a future
extension worse; if it was non-negative, extending by $x$ is at least as good as
starting anew. Taking the maximum over all $cur$ values yields the global
optimum $best$.

**Edge cases.**\
Initialize $best$ with the first element to handle all-negative inputs
correctly. No extra imports or data structures are required.

**Complexity.**\
Time $O(n)$, space $O(1)$.

## Equivalent views

**Prefix-minimum (greedy via prefix sums).**\
Let $S[i]$ be the prefix sum up to $i$. The best subarray ending at $i$ is $$
S[i] - \min_{0 \le k < i} S[k].
$$

Maintaining the running minimum prefix produces the same $O(n)$ algorithm as
Kadane.

**Dynamic programming with an explicit array.**\
Define $dp[i]$ as the maximum sum of a subarray ending at $i$: $$
dp[i] = \max(nums[i],\ nums[i] + dp[i-1]).
$$

The answer is $\max_i dp[i]$. This is Kadane with $O(n)$ memory; compressing to
a single `cur` variable restores $O(1)$ space.

## Summary

- Brute force with a running sum: time $O(n^2)$, space $O(1)$.
- Kadane / prefix-minimum: time $O(n)$, space $O(1)$ — recommended.
- DP array is conceptually the same as Kadane but uses $O(n)$ memory.
