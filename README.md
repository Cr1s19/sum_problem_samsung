# 🤩 Problem: Max Pair Sum with Matching First and Last Digits

## Description

Given an array of *positive integers, find the **maximum sum* of any two *distinct elements* such that *both the first digit* (most significant digit) and the *last digit* (least significant digit) of the numbers *match*.

If no such valid pair exists, return -1.

This problem involves grouping numbers by a shared (first_digit, last_digit) pattern. By organizing numbers using this key, we can efficiently track the top two values per group and compute the maximum possible sum.

---

## Input

* nums: a list of integers where 1 <= nums[i] <= 10^9
* 2 <= len(nums) <= 10^5

## Output

* Return an integer: the *maximum sum* of any valid pair, or -1 if no such pair exists.

---

## Examples

### Example 1

python
Input: [300, 300]
Output: 600
# First digit: 3, Last digit: 0 → match
# Sum = 300 + 300 = 600


### Example 2

python
Input: [101, 1991]
Output: 2092
# 101 → First: 1, Last: 1
# 1991 → First: 1, Last: 1
# Valid pair → 101 + 1991 = 2092


### Example 3

python
Input: [123, 132, 321]
Output: -1
# No pair shares both first and last digits


---

## Edge Cases

* Single element → no valid pair → return -1
* Multiple values in a group → choose *two largest*
* Input only includes *positive integers* (no negatives)

---

## Complexity

* *Time*: O(n × d) where d is the number of digits (at most 10)
* *Space*: O(100) for at most 10 × 10 digit pair groupings

---

## Extension: Handling Negatives

If negative numbers are allowed, convert to string using absolute value:

python
s = str(abs(x))
first, last = s[0], s[-1]
