def largest_product(grid, n):
    max_product = None

    num_rows = len(grid)
    num_cols = len(grid[0])

    if max_product is None or product > max_product:
        max_product = product


    for row in range(num_rows):
        for col in range(num_cols - n + 1): 
            product = 1
            for i in range(n):
                product *= grid[row][col + i]
            if product > max_product:
                max_product = product


grid = [
    [1, 2,  3,  4,  5],
    [6, 7,  8,  9,  8],
    [1, 99, 88, 77, 5],
    [1, 2,  3,  4,  5],
    [1, 6,  7,  8,  9],
]
n = 3
expected = 670824  # 99 * 88 * 77
assert largest_product(grid, n) == expected

grid = [
    [1, 2,  3,  4],
    [5, 6,  7,  8],
    [9, 10, 11, 12]
]
n = 3
expected = 1320  # 10 * 11 * 12
assert largest_product(grid, n) == expected

grid = [
    [13, 0, 9],
    [2,  6, 10],
    [3,  7, 11],
    [4,  8, 12]
]
n = 3
expected = 1320  # 10 * 11 * 12
assert largest_product(grid, n) == expected

grid = [
    [1, 99, 9],
    [2, 77, 10],
    [3, 22, 11],
    [4, 0,  12]
]
n = 2
expected = 7623  # 99 * 77
assert largest_product(grid, n) == expected

grid = [
    [1, 2, 3],
    [4, 5, 6]
]
n = 3
expected = 120  # 4 * 5 * 6
assert largest_product(grid, n) == expected

grid = [
    [-1],
    [2],
    [-3]
]
n = 2
expected = -2  # -1 * 2
assert largest_product(grid, n) == expected

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
