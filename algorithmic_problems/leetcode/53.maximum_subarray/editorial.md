# 53. Maximum Subarray — Editorial

**Idea (Kadane’s Algorithm).** Maintain the best suffix sum ending at `i` and
the best overall answer. For each `x` in `nums`, either extend the current
subarray (`cur + x`) or start fresh at `x`: `cur = max(x, cur + x)`. Track
`best = max(best, cur)`.

**Correctness sketch.** At step `i`, `cur` is the maximum sum of a subarray that
**must** end at `i`. Any optimal subarray ending at `i` is either:

1. the previous optimal suffix ending at `i-1` extended by `x`, or
2. a new subarray starting at `i` (when previous sum is harmful). Taking the max
   of these two maintains the invariant. `best` is the max over all
   suffix-optimal values, hence the global optimum.

**Complexity.** `O(n)` time, `O(1)` extra space.

## Dynamic Programming (explicit dp array) — Details

Idea. Let dp[i] be the maximum-sum subarray that ends at index i. Either we
extend the best subarray ending at i-1 or we start fresh at i:

$dp[i] = \max(\text{nums}[i],\ \text{nums}[i] + dp[i-1])$.

dp[i]=max(nums[i], nums[i]+dp[i−1]).

Initialize dp[0] = nums[0] (copying nums into dp does this implicitly), and the
answer is max(dp).

Relation to Kadane. This is the same recurrence as Kadane’s algorithm; Kadane
keeps only the last value (cur) instead of the whole dp array, reducing space to
`O(1)`.

Complexity. `O(n)` time, `O(n)` extra space (`O(1)` if you compress to Kadane).

## Brute Force baselines

A simple baseline is to enumerate subarrays.

`O(n²)` with running sum. Fix a start i, then extend the end j ≥ i while keeping
a running sum:

This checks all `n(n+1)/2` subarrays and maintains each sum in `O(1)` amortized
per extension.

Note. A naive triple-loop that recomputes sums from scratch is `O(n³)` and is
only for pedagogy; the running-sum version above is the practical brute-force
baseline.

Comparison. Brute force is easy to reason about but too slow for large n;
DP/Kadane achieves `O(n)` time.
