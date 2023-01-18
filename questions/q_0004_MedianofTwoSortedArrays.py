import sys


class Solution:
    """
    4. Median of Two Sorted Arrays

    Difficulty: Hard

    Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

    The overall run time complexity should be `O(log (m+n))`.

    Example 1:
    ```
    Input: nums1 = [1,3]; nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.
    ```
    Example 2:
    ```
    Input: nums1 = [1,2]; nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
    ```
    Example 3:
    ```
    Input: nums1 = []; nums2 = [1]
    Output: 1
    Explanation: merged array = [1] and median is 1.
    ```
    Example 4:
    ```
    Input: nums1 = []; nums2 = [2,3]
    Output: 2.5
    Explanation: merged array = [2,3] and median is (2 + 3) / 2 = 2.5.
    ```

    Constraints:
    - `nums1.length == m`
    - `nums2.length == n`
    - `0 <= m <= 1000`
    - `0 <= n <= 1000`
    - `1 <= m + n <= 2000`
    - `-106 <= nums1[i], nums2[i] <= 106`
    """

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:  # type: ignore
        m = len(nums1)
        n = len(nums2)
        pointer1 = 0
        pointer2 = 0
        merged_array = []
        median_indices = (
            [(m + n) // 2] if (m + n) % 2 == 1 else [(m + n) // 2 - 1, (m + n) // 2]
        )
        while len(nums1) > 0 or len(nums2) > 0:
            if (len(nums1) > 0 and len(nums2) > 0 and nums1[0] < nums2[0]) or len(
                nums2
            ) == 0:
                merged_array.append(nums1.pop(0))
                pointer1 += 1
            elif (len(nums1) > 0 and len(nums2) > 0 and nums1[0] >= nums2[0]) or len(
                nums1
            ) == 0:
                merged_array.append(nums2.pop(0))
                pointer2 += 1
            if len(merged_array) == median_indices[-1] + 1:
                if (m + n) % 2 == 1:
                    return merged_array[median_indices[0]]
                else:
                    return (
                        merged_array[median_indices[0]]
                        + merged_array[median_indices[1]]
                    ) / 2
