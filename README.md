# CodeKata
Each branch contains an exercise, which is solved by TDD that generates a matching production code module with it.

## Kata 002

This is the n islands problem. Given a 2D Array, where 1's are land, and 0's are water,
return the number of islands made up in this array.

```
Input: 
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

This example is taken from leetcode. Utilizing the DFS (Depth First Search),
return the number of islands in this grid.
