<!-- METADATA -->

<!-- based on template v0.0 -->

<!-- Objectives
- Introduce the fundamentals of competitive programming.
- Explain what ICPC is, including its rules and the participation process.
- Illustrate how to approach competitive programming problems and provide a
  starter template.
- Show how to use platforms such as Codeforces and interpret submission
  results.
- Share strategies for effective training and guidance on how to seek help.
- Provide advice against common beguineer mistakes.
-->

[cph]: https://cses.fi/book/book.pdf

# Introduction to Competitive Programming

`25/Sep/2025`

---

Competitive programming (CP) is a mind-sport where participants solve
algorithmic and mathematical problems by programming efficient solutions under
time and memory constraints.

## Is it Worth Your Time?

Becoming good at CP requires consistent effort, patience, and discipline. Along
the way, you have to deeply study algorithms, learn how to write efficient code,
and enhance your algorithmic problem-solving skills.

By practicing CP you not only become a stronger programmer, but become a better
candidate for programmer jobs, as you practice the core skill evaluated in tech
interviews, and many companies hold in high regard awards in CP. But it's very
demanding, and to truly enjoy the journey you should be genuinely interested in
the problem solving process, and have a competitive spirit towards it.

In the end, every problem you solve is a small victory, and every contest is an
opportunity to learn and improve yourself. Stay consistent, stay curious, and
you’ll find that the discipline and resilience you build here will serve you far
beyond the competitions themselves.

## What is ICPC?

The International Collegiate Programming Contest (ICPC) is the world’s largest
and most prestigious CP competition for university students. Teams of three
(with the option of a reserve member), along with their coach, work together to
solve challenging algorithmic problems within a fixed time limit (usually 5
hours).

### How to Participate?

To participate, form a team of three members plus a coach. Registration is
handled through the official [ICPC website](https://icpc.global). Each region
has its own qualifying contests (often called Regionals), which lead to the
World Finals.

In Mexico, the ICPC journey begins with the Gran Premio de México, a national
series made up of three rounds. Teams from across the country participate in
these contests, earning points at each event, their cumulative score determines
whether they qualify for the ICPC Mexico Finals (regional). The top-performing
teams from the Finals advance to the Latin America Championship (LAC) (super
regional), and the very best continue on to the ICPC World Finals.

To prepare for these contests, many participants take part in the Training Camp
Mexico (TCMX). This bootcamp brings together CP teams for intensive practice and
mentorship.

Check out the ICPC MX [contact](https://pda2024.icpcmexico.org/en/contact/)
channels for the registration dates.

## How to Approach Problems?

Before touching the keyboard, start by understanding what you are being asked,
failing to fully understand the given problem is catastrophic (and also a very
common mistake). After understanding your goal, reason about the problem by
reducing the different parts of the problem to what you know (easier said than
done).

### Time and Space Analysis

When you come up with ideas, first ensure that they fit the in time and space
constraints, the rule of thumb is that for every second a computer can perform
$10^8$ operations, where an operation is an instruction considered to be $O(1)$.
This implies that you cannot write or read more than $10^8$ elements from
memory. To estimate the operations your solution will take, calculate the time
complexity, and evaluate that function by the worst case (most of time that is
the biggest $n$), for example, a $O(n^2)$ solution with $n \le 10^5$ will exceed
1 second.

### Testing Solutions in Paper

Next briefly test your solution by hand with edge cases to ensure it will work,
think of the worst possible cases on time and space, abnormal circumstances
which may cause undefined behaviour (UB) in your code, like arithmetic overflows
or invalid memory access access.

Now you have to code your solution, make sure to have a clear idea of the code
beforehand, this helps you to notice if your solution is even programmable (it
may be too long and complicated or straight impossible).

If your submission is wrong take a step back, consider more edge cases, try to
test them locally, or review your proposed solution.

## Programming for CP

Due to the particular set of constraints found in CP, code written for problems
is not the same as other purposes, most importantly one must take into
consideration the approximated performance on large inputs, and as time is of
essence, it has to be written very fast.

### Which Language Should You Use?

Objectively, C++. It's the best language for CP because of its performance,
algorithm and data structure rich standard library and ease for parsing input.
Although, its fine to start with a language you are more familiar with, but it's
highly advised that you eventually transition to C++.

The C++ needed to get started with CP comes down to the basic constructs of the
language (arithmetic, flow control, IO, etc), and the Standard Template Library
(STL), nothing more. You will eventually use more obscure features (even dark
magic), but certainly not at the beginning. Lastly, its recommended to use g++
as your compiler, as it has useful extensions (like `bits/stdc++.h`).
[Competitive Programmer’s Handbook](cph) contains an excellent introduction to
the C++ required for CP.

> From the beginning, make the effort to understand the bit level details.

### C++ Template

In competitions you are usually allowed to have printed material, such as books,
implementations of algorithms, and most importantly, a template with base
utilities for programming. This is a very simple one, with time you will develop
your own.

```cpp
// compiles with c++ version 17
// reads input from "in" and writes output to "out"
// g++ --std=c++17 x.cpp && ./a.out <in> out
// provided by GNU libstdc++, includes most standard lib headers
#include <bits/stdc++.h>

// avoids typing "std::", beware the name collisions
using namespace std;

// Fast IO, unsynchronizes cin and cout with C IO
#define FIO                                                        \
  ios_base::sync_with_stdio(0); /* false */                        \
  cin.tie(0);                   /* nullptr */                      \
  cout.tie(0);                  /* nullptr */

// type alias for commonly used long-named types
typedef long long lli;
typedef long double ld;

// use perr(<var>) for debugging
// does nothing when compiled by the online judge
#ifndef ONLINE_JUDGE
#define perr(x) cerr << #x << " " << (x) << endl
#else
#define perr(x) 0
#endif // !ONLINE_JUDGE

// compacts very common loops
#define fora(i, a, b) for(lli i = (a); (i) < (b); ++i) // [a -> b)
#define ford(i, a, b) for(lli i = (a); (i)-- > (b);)   // [b <- a)

int main() {FIO;
  /* problem */
  return 0;
}
```

### C++ Toolchain and Debugging

To efficiently compile and test your code before submissions you can use many
tools.

- The compiler: Learn how to use the compiler effectively, how to understand
  it's errors, and what flags are useful, like `-fsanitize=address` (sometimes
  even used by judges).

- The debugger: Use gdb for inspecting otherwise hard to print logic and state,
  it may be hard to pick up, but you can completely inspect every variable and
  flow control of your program. Use `-g` to compile with debugging symbols.

- Printing output: This classic debugging method is recommended for fast
  debugging and its useful when under a lot of preassure. Tip, use `cerr` (or
  the `perr(x)` macro) instead of cout to separate your output from debugging
  prints.

## Practice Platforms

Online judges, problem sets, contest pages, are all web pages in which you can
practice CP by solving problems, there are different styles, like tagged problem
sets (separated by topics), randomized problems, problems ranked by difficulty,
contest simulations, etc.

- [**Codeforces**](https://codeforces.com/): Frequent contests, large archive of
  problems sorted by difficulty, biggest CP community.
- [**Codeforces GYM**](https://codeforces.com/gyms): Past competitions, like
  ICPC contests.
- [**AtCoder**](https://atcoder.jp/): Quality problems, weekly contests, clean
  difficulty rating system.
- [**CSES Problem Set**](https://cses.fi/problemset/): Curated set of ~400
  problems, excellent for learning the base techniques.
- [**SPOJ (Sphere Online Judge)**](https://www.spoj.com/): Huge archive,
  includes classical problems and user-created ones.

### Judge Results

When you submit a solution on these platforms, you’ll usually get one of the
following results:

AC (Accepted): ✅ Your solution is correct and meets time/memory limits.

WA (Wrong Answer): ❌ The program ran but produced an incorrect output on at
least one test case.

TLE (Time Limit Exceeded): ⏱️ Your program didn’t finish in the allowed time.
Usually means your algorithm is too slow.

MLE (Memory Limit Exceeded): 💾 Your solution used more memory than allowed
(e.g., large arrays, recursion depth).

RE (Runtime Error): ⚠️ Your program crashed (segmentation fault, division by
zero, array out-of-bounds, etc.).

CE (Compilation Error): 🛠️ The code didn’t compile on the judge’s system (often
due to syntax errors or using non-standard libraries).

## How to Practice Efficiently

This is very opinionated, many people suggest different strategies and methods
to follow, in the end, your goal should be to learn and get better at solving
increasingly difficult problems, any reasonable strategy in which notice notice
improvement is likely a good path.

Specially when starting, there are many strategies like.

```
try to solve the problem, if stuck/no-ideas for x time, read the answer/hints
```

Although it may seem reasonable, you are not learning how to solve problems, you
just let someone else think the answer for you. This is why many great
competitive programmers recommend to forget about editorials at all, but whether
you want to follow that advice or not, use that strategy with moderation. If you
feel stuck in a lot of problems, take a step back and try to think why that is,
sometimes talking with someone who has overcomed those difficultities may help
you. This is a recommended [blog](https://codeforces.com/blog/entry/98621) on
this topic.

Good places to start are [codeforces EDU](https://codeforces.com/edu/course/2)
(make sure to watch the theory before solving the first problems), and reading
[Competitive Programmer’s Handbook](cph) while doing
[cses](https://cses.fi/problemset/) problems.

## Common Pitfalls

- Comparing yourself with others. Everyone is different, focus on your
  improvement.
- Reading too much Theory. If you want to solve `problems`, practice
  `problem-solving`.
- Learning too advanced techniques. Most problems are solved with the basic
  techniques, and if you are still a beginner you are unlikely to take advantage
  of advanced algorithms.
- Avoid Burnout. Be reasonable and consistent on the time you want to practice,
  practicing too many hours a day is unsustainable for most people.

---

## Bibliography

- [A Guide to Competitive Programming](https://www.reddit.com/r/csMajors/comments/z4qjzx/a_guide_to_competitive_programming/)
- [Starting Competitive Programming - Steps and
  Mistakes](https://www.youtube.com/watch?v=bVKHRtafgPc)
- [Self-deception: maybe why you're still grey after practicing every day](https://codeforces.com/blog/entry/98621)

## Additional Resources

- [Competitive Programmer’s Handbook](cph)
- [How to start Competitive Programming? For
  beginners!](https://www.youtube.com/watch?v=xAeiXy8-9Y8)
- [From Beginner to Grandmaster - Complete Roadmap for Competitive
  Programming](https://www.youtube.com/watch?v=bSdp2WeyuJY)

## Authors

- Sebastian Certuche @sebascert
