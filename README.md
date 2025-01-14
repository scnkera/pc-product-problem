# Product Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

We are interested in finding the largest product of a contiguous vertical or horizontal sequence of numbers in a grid.

Your function will be given two arguments, a list of lists of integers and a number of elements in a sequence to find the product of.

For example:

```py
grid = [
    [1, 2,  3,  4,  5],
    [6, 7,  8,  9,  8],
    [1, 99, 88, 77, 5],
    [1, 2,  3,  4,  5],
    [1, 6,  7,  8,  9],
]
n = 3
```

Because n = 3, our sequence must include exactly 3 factors. The three contiguous numbers that form the highest product are 99, 88, and 77, giving us a maximum product of 670824. Therefore, our function should return 670824.

Note that the numbers can be contiguous horizontally OR vertically. However, diagonal numbers will NOT be considered contiguous.

Inspired by https://projecteuler.net/problem=11

## Examples

### Example 1

```py
grid = [
    [1, 2,  3,  4,  5],
    [6, 7,  8,  9,  8],
    [1, 99, 88, 77, 5],
    [1, 2,  3,  4,  5],
    [1, 6,  7,  8,  9],
]
n = 3
largest_product(grid, n)
```

Produces

```py
670824  # 99 * 88 * 77
```

### Example 2

```py
grid = [
    [1, 2,  3,  4],
    [5, 6,  7,  8],
    [9, 10, 11, 12],
]
n = 3
largest_product(grid, n)
```

Produces

```py
1320  # 10 * 11 * 12
```

### Example 3

```py
grid = [
    [13, 0, 9],
    [2,  6, 10],
    [3,  7, 11],
    [4,  8, 12],
]
n = 3
largest_product(grid, n)
```

Produces

```py
1320  # 10 * 11 * 12
```

### Example 4

```py
grid = [
    [1, 99, 9],
    [2, 77, 10],
    [3, 22, 11],
    [4, 0,  12],
]
n = 2
largest_product(grid, n)
```

Produces

```py
7623  # 99 * 77
```

### Example 5

```py
grid = [
    [1, 2, 3],
    [4, 5, 6],
]
n = 3
largest_product(grid, n)
```

Produces

```py
120  # 4 * 5 * 6
```

### Example 6

```py
grid = [
    [-1],
    [2],
    [-3],
]
n = 2
largest_product(grid, n)
```

Produces

```py
-2  # -1 * 2
```
