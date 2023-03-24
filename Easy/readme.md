## 1. twosum.py
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.
You may assume that each input would have ***exactly one solution***, and you may not use the same element twice.
You can return the answer in any order.
### Example 1:

`Input: nums = [2,7,11,15], target = 9`

`Output: [0,1]`

`Output: Because nums[0] + nums[1] == 9, we return [0, 1].`
### Example 2:

`Input: nums = [3,2,4], target = 6`

`Output: [1,2]`
### Example 3:

`Input: nums = [3,3], target = 6`

`Output: [0,1]`
 

### Constraints:
- 2 <= nums.length <= 104
- 109 <= nums[i] <= 109
- 109 <= target <= 109
- `Only one valid answer exists.`
---
## 2. Reverse_Integer.py
Given a signed 32-bit integer `x`, return x with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return `0`.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

### Example 1:

`Input: x = 123`

`Output: 321`
### Example 2:

`Input: x = -123`

`Output: -321`
### Example 3:

`Input: x = 120`

`Output: 21`
### Example 4:

`Input: x = 0`

`Output: 0`
 

### Constraints:
- `-2^31 <= x <= 2^31 - 1`
--- 
## 3. Palindrome_Number.py
Given an integer `x`, return `true` if `x` is `palindrome` integer.
An integer is a palindrome when it reads the same backward as forward. For example, `121` is palindrome while `123` is not.
 
### Example 1:

`Input: x = 121`

`Output: True`
### Example 2:

`Input: x = -121`

`Output: False`

`Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.`
### Example 3:

`Input: x = 10`

`Output: False`

`Explanation: Reads 01 from right to left. Therefore it is not a palindrome.`
### Example 4:

`Input: x = -101`

`Output: False`
 

### Constraints:
- `-2^31 <= x <= 2^31 - 1`
---
## 4.Roman_to_Integer.py
Roman numerals are represented by seven different symbols: `I, V, X, L, C, D and M`.

`'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000`

For example, `2` is written as `II` in Roman numeral, just two one's added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

### Example 1:

`Input: s = "III"`

`Output: 3`
### Example 2:

`Input: s = "IV"`

`Output: 4`
### Example 3:

`Input: s = "IX"`

`Output: 9`
### Example 4:

`Input: s = "LVIII"`

`Output: 58`

`Explanation: L = 50, V= 5, III = 3.`
### Example 5:

`Input: s = "MCMXCIV"`

`Output: 1994`

`Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.`
 

### Constraints:

- ` <= s.length <= 15`
- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
- It is **guaranteed** that s is a valid roman numeral in the range `[1, 3999]`.
---
## 5. Valid_Parentheses.py

Given a string `s` containing just the characters `'(', ')', '{', '}', '['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. n brackets must be closed in the correct order.
 

### Example 1:

`Input: s = "()"`

`Output: True`

### Example 2:

`Input: s = "()[]{}"`

`Output: True`
### Example 3:

`Input: s = "(]"`

`Output: False`

### Example 4:

`Input: s = "([)]"`

`Output: False`

### Example 5:

`Input: s = "{[]}"`

`Output: True`
 
### Constraints:
- `1 <= s.length <= 104`
- `s` consists of parentheses only `'()[]{}'`.
---
## 6. Remove_Duplicates_from_Sorted_List.py
Given the `head` of a sorted linked list, *delete all duplicates such that each element appears only once*. Return the *linked list* **sorted** as well.

### Example 1:
![list1](https://user-images.githubusercontent.com/69154768/124506993-76ca7e80-ddea-11eb-836b-abc3d24a7f16.jpg)

`Input: head = [1,1,2]`

`Output: [1,2]`

### Example 2:
![list2](https://user-images.githubusercontent.com/69154768/124507025-8ba71200-ddea-11eb-807e-2c2a1c17e832.jpg)

`Input: head = [1,1,2,3,3]`

`Output: [1,2,3]`

### Constraints:
- The number of nodes in the list is in the range `[0, 300]`.
- `-100 <= Node.val <= 100`
- The list is guaranteed to be *sorted* in *ascending order*.
---
## 7. Merge_Sorted_Array.py

You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.
**Merge** `nums1` and `nums2` into a single array sorted in `non-decreasing order`.
The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

### Example 1:

`Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3`

`Output: [1,2,2,3,5,6]`

`Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.`

### Example 2:

`Input: nums1 = [1], m = 1, nums2 = [], n = 0`

`Output: [1]`

`Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].`

### Example 3:

`Input: nums1 = [0], m = 0, nums2 = [1], n = 1`

`Output: [1]`

`Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.`
 
### Constraints:

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-109 <= nums1[i], nums2[j] <= 109`
---
## 8. Pascal's_Triangle.py

Given an integer `numRows`, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

### Example 1:

`Input: numRows = 5` 

`Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]`

### Example 2:

`Input: numRows = 1`

`Output: [[1]]`
 
### Constraints:

- `1 <= numRows <= 30`
---
## 9. Island_Perimeter.py

You are given a `row x col` grid representing a map where `grid[i][j] = 1` represents land and `grid[i][j] = 0` represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

### Example 1:

`Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]`

`Output: 16`

### Example 2:

`Input: grid = [[1]]`

`Output: 4`

### Example 3:

`Input: grid = [[1,0]]`

`Output: 4`

### Constraints:

- `row == grid.length`
- `col == grid[i].length`
- `1 <= row, col <= 100`
- `grid[i][j] is 0 or 1.`
- There is exactly one island in `grid`.
---
