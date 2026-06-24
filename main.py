"""
Prefix Sum + Hash Map

Problem:
Given an integer array nums and an integer k,
count how many continuous subarrays have sum equal to k.

Example:
nums = [1, 2, 3, -1, 2]
k = 3

Valid subarrays:
[1, 2]
[3]
[2, 3, -1, -1?]  # not in this example
"""

from typing import List


def count_subarrays_sum_k(nums: List[int], k: int) -> int:
    """
    Count the number of continuous subarrays whose sum equals k.

    Core idea:
    current_prefix - previous_prefix = k

    So:
    previous_prefix = current_prefix - k

    We use a hash map to record how many times each prefix sum
    has appeared before.
    """

    prefix_sum = 0
    count = 0

    # key: prefix sum
    # value: how many times this prefix sum appeared
    seen_prefix = {0: 1}

    for x in nums:
        prefix_sum += x

        need = prefix_sum - k

        if need in seen_prefix:
            count += seen_prefix[need]

        seen_prefix[prefix_sum] = seen_prefix.get(prefix_sum, 0) + 1

    return count


if __name__ == "__main__":
    nums = [1, 2, 3, -1, 2]
    k = 3

    result = count_subarrays_sum_k(nums, k)

    print("nums =", nums)
    print("k =", k)
    print("number of subarrays =", result)
