[# 2028. Find Missing Observations](https://leetcode.com/problems/find-missing-observations/)
You have observations of <code>n + m</code> **6-sided** dice rolls with each
face numbered from 1 to 6. <code>n</code> of the observations went missing, and
you only have the observations of <code>m</code> rolls. Fortunately, you have
also calculated the **average value** of the <code>n + m</code> rolls.

You are given an integer array <code>rolls</code> of length <code>m</code> where
<code>rolls[i]</code> is the value of the $i^{th}$ observation. You are also
given the two integers <code>mean</code> and <code>n</code>.

Return _an array of length <code>n</code> containing the missing observations
such that the **average value** of the <code>n + m</code> rolls is **exactly**
mean. If there are multiple valid answers, return any of them. If no such array
exists, return an empty array_.

The **average value** of a set of <code>k</code> numbers is the sum of the
numbers divided by <code>k</code>.

Note that mean is an integer, so the sum of the <code>n + m</code> rolls should
be divisible by <code>n + m</code>.

> [!fingerprint]+ Examples Example one
>
> ```python
> Input: rolls = [3,2,4,3], mean = 4, n = 2
> ```

Output: [6,6] Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 +
6 + 6) / 6 = 4.

> ````
> Example two
> ```python
> ````

Input: rolls = [1,5,6], mean = 3, n = 4 Output: [2,3,2,2] Explanation: The mean
of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.

> ````
> Example three
>  ```python
> ````

Input: rolls = [1,2,3,4], mean = 6, n = 4 Output: [] Explanation: It is
impossible for the mean to be 6 no matter what the 4 missing rolls are. ```

## Solution

For this problem, the **approach is mathematical**.

### Naive Solution

A naive solution to this problem would be to try all possible combinations of
$n$ dice values (each between 1 and 6) and check which combinations produce a
total sum equal to missing_sum. In other words, it would perform a brute-force
search over all $6n$ possible outcomes, selecting those that satisfy the sum
constraint. While this guarantees finding all valid solutions, it quickly
becomes computationally infeasible as $n$ grows, since the number of
combinations grows exponentially.

### Proposed solution

First let's understand that the mean will be the overall mean of all
<code>n+m</code>. By definition, the mean can be calculated for this problem as:
$$
\text{mean} = \frac{\text{total sum of all rolls}}{n + m}
$$

and then we can say that the **expected total sum** of all dice rolls is: $$
\text{total\_sum} = \text{mean} \times (n + m)
$$

Which can be found in the code as:

```python
total_sum = mean * (n + m)
```

Then, we can define the sum of the known rolls, as: $$
\text{observed\_sum} = \sum(\text{rolls})
$$

Hence, the **sum of the missing rolls** must be: $$
\text{missing\_sum} = \text{total\_sum} - \text{observed\_sum}
$$

In python would be:

```python
observed_sum = sum(rolls)
missing_sum = total_sum - observed_sum
```

Now, we need to understand that each die roll can only take values between **1
and 6**.\
Therefore, the total sum of missing rolls must satisfy:

$$n\leq \text{missing\_sum} \leq 6n$$

If not, there’s **no possible solution**.

This constraint can be programmed as:

```python
if missing_sum < n or missing_sum > 6 * n:
    return []
```

Now, the `missing_sum` will be split into $n$ integers between 1 and 6, as
evenly as possible.

Mathematically, we want to find integers $x_1, x_2, \dots, x_n$ such that:

$$
\sum_{i=1}^{n} x_i = \text{missing\_sum}
$$

and $$
1 \leq x_i \leq 6 \quad \forall i \in \{1, 2, \dots, n\}
$$

Each $x_i$ will be as close as possible to the average value: $$
\frac{\text{missing\_sum}}{n}
$$

We can compute:

- The **base value** (average part per roll)
- The **remainder** (how many rolls need +1 to reach the exact total)

Using integer division and modulo: $$
\text{base}, \text{extra} = \text{divmod}(\text{missing\_sum}, n)
$$

So:

- `base` = integer division result (each roll gets at least this value)
- `extra` = remainder (the number of rolls that get one extra point)

In the code:

```python
base, extra = divmod(missing_sum, n)
result = [base] * n
for i in range(extra):
    result[i] += 1
```

At the end, `result` satisfies:

$$
\sum(\text{result}) = \text{missing\_sum}
$$

and all values are integers between 1 and 6 (if the case was feasible).
