# [829. Consecutive Numbers Sum](https://leetcode.com/problems/consecutive-numbers-sum/)

### Naive Solution

The most naive approach would be to try all consecutive numbers sequences less
than $n$, with complexity of $O(n^2)$, this is extremely inefficient for our
input size.

### Sliding Window

An optimization would be to use a sliding window algorithm which can optimize
the search complexity down to $O(n)$, by comparing the sum of a dynamic window
increasing to the right when $sum < n$ and decreasing froom the left when $sum >
n$, finally we would only need to count every occurrence of $sum = n$. This
approach it's still far from optimal as $n$ a is very large number.

### Sum Decomposition (sol 1)

> For reference, See the Sums sections in the
> [Discrete Math resources](../../../resources/math/discrete_math.md).
> Mathemathics for Computer Science (MIT) lecture 05 is specially recommended.

In order to optimize the solution we need to analyze it mathematically, notice
that the sum of consecutive numbers has a closed form which derives from the
gaussian sum.

$$
\sum_{i=a}^{a+m-1} i = \sum_{i=1}^{a+m-1} i - \sum_{i=1}^{a-1} i = \frac{(a+m-1)(a+m)}{2} - \frac{a(a-1)}{2}
$$

$$
\frac{a^2+am-a+am+m^2-m-a^2+a}{2} = \frac{m^2+2am-m}{2} = am + \frac{m(m-1)}{2} = n
$$

$$
(a+0) + (a+1) + (a+2) + ... + (a+m-2)+ (a+m-1)
$$

Where $a$ is the first consecutive number, and the sum consists of $m$ numbers.
Now we only need to find every pair of numbers $(a\,m)$ to find a solution.

By the definition of the problem we know that every variable must be an integer,
so we can isolate $a$ in terms of $m$ and $n$, and test if the result is an
integer, if it is, we have found a valid pair.

$$
a = \frac{2n+m-m^2}{2m}
$$

We can find all solutions by iterating from one up to when
$\frac{m^2+m}{2} \le n$ (obtained by setting $a=1$). This approach optimizes the
solution down to $O(\sqrt{n})$, but we can do even better.

### Odd Factors of $n$ (sol 2)

Notice that from the derived expression $m(m+2a-1)=2n$ we can deduce that either
$m$ or $m+2a-1$ must be odd, they cannot be even at the same time as
$2(\frac{m}{2}+a)-1$ is odd.

This means that there are as many valid sums as there are odd factors of $n$, we
just have to count them. The algorithm for computing this is described as
follows.

First we discard every even factor, by succesivly halving the $n$ until its odd,
which is a logarithmic operation.

Then we iterate through every odd number until $\sqrt{n}$ (this is for
simplicity, as we could've also factorize $n$ which has the same time
complexity), finding every odd factor in the process, and optimizing the search
by dividing by a factor every time it's found, which greatly reduces the search
space for most numbers.

Whenever we find a factor of $n$ we multiply the count of factors by it's
occurrences, as every possibility of factoring $n$ either contains the newly
found factor, or not.

The algorithm still has $O(\sqrt{n})$ in the cases of specially hard to factor
numbers, such as perfect squares, as it has to iterate until it finds the factor
$\sqrt{n}$, but by taking advantage of factorization, most commonly occurring
numbers will be reduced logarithmically, which yields better runtimes than the
previous one.
