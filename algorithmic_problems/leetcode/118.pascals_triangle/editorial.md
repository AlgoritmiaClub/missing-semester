# [118. Pascal’s Triangle](https://leetcode.com/problems/pascals-triangle/)

**Problem.**  
Given an integer `numRows`, return the first `numRows` of Pascal’s Triangle.  

In Pascal’s Triangle, each number is the sum of the two numbers directly above it.  

Example:

```bash
Input: numRows = 5
Output:
[
[1],
[1,1],
[1,2,1],
[1,3,3,1],
[1,4,6,4,1]
]
```

### Building up to the solution

**Things to take into account...**
- The top-most row consists on a single number `1`.
- Each row begins and ends with `1`.  
- The inner elements of a row are the sum of the two numbers directly above it from the previous row. 
- A row's values are only dependant on the values that are directly above it.

If you visualize the triangle:

```bash
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```

you can see that every non-edge number has two parents above it: one to the left and one to the right.

Let's remember that, in order to construct the `i`-th row, we only need the `(i-1)`-th row.

So, accessing the desired row in any given iteration where $i > 0$, can be done by:

```bash
desired_row = triangle[i - 1]
```

Given that `desired_row` is just a list, we can access its elements by doing the following:

```bash
desired_element_from_row = desired_row[j]
```

$0 \le j < \text{len(desired\_row)}$

Hence:

```bash
desired_element_from_row = triangle[i - 1][j]
```


### Approach
 
For every row `i`:
1. Initialize a list of size `i + 1` filled with `1`s.
2. For every inner index `j` in that row, compute  
   `row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]`.
3. Append the constructed row to `triangle`.

# Complexity

- Time complexity: $O(n^2)$

    The total number of elements in the triangle is
    $1 + 2 + 3 + … + n = \frac{n(n+1)}{2} = O(n^2)$.

- Space complexity: $O(n^2)$

    We do need to store all rows of the triangle.