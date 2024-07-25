#!/usr/bin/python3
"""
0. Pascal's Triangle
"""

def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    
    res = [[1]]

    for i in range(1, n):
        row = [1]
        last_row = res[i - 1]
        
        for j in range(1, i):
            row.append(last_row[j - 1] + last_row[j])
        
        row.append(1)
        res.append(row)

    return res
