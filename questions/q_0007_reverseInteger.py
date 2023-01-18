class Solution:
    """Given a signed 32-bit integer `x`, return `x` *with its digits
    reversed*. If reversing `x` causes the value to go outside the signed
    32-bit integer range `[-231, 231 - 1]`, then return `0`.

    **Assume the environment does not allow you to store 64-bit integers
    (signed or unsigned).**



    **Example 1:**

        Input: x = 123
        Output: 321

    **Example 2:**

        Input: x = -123
        Output: -321

    **Example 3:**

        Input: x = 120
        Output: 21



    **Constraints:**

    -   `-231 <= x <= 231 - 1`"""

    def reverse_bitwise_operation(self, x: int) -> int:
        """The maximum value of a signed 32-bit integer can take is `0x7fff_ffff`, while its minimum value is `-0x8000_0000`.

        When a negative x is in range, the operation (`x & -0x8000_0000`) always returns `-0x8000_0000`, whereas when a positive x is in range, the operation (`x & 0x7fff_ffff`) returns x.

        Thus, in this approach, we try to reverse the digits of the absolute value of x, while checking if the resulting reversed number (with the appropriate sign) satisfies the above condition. If it does not, we return a `0`.

        Args:
            x (int): A signed 32-bit integer whose digits need to be reversed.

        Returns:
            int: The reversed 32-bit integer. If the reversed number is out of range for a 32-bit integer, `0` is returned.

        Time Complexity:
            O(log(x)): As there are approximately `log10(x)` number of digits in x.

        Space Complexity:
            O(1):
        """
        maxLim = 0x7FFF_FFFF
        minLim = -0x8000_0000
        answer = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            answer = x % 10 + answer * 10
            if answer != 0 and (
                (sign == 1 and (((answer * sign) & maxLim) != (answer * sign)))
                or (sign == -1 and (((answer * sign) & minLim) != minLim))
            ):
                return 0
            x //= 10
        return sign * answer

    def reverse(self, x: int) -> int:
        """The maximum value of a signed 32-bit integer can take is `0x7fff_ffff`, while its minimum value is `-0x8000_0000`.

        Thus, in this approach, we try to reverse the digits of the absolute value of `x`, while checking if the resulting reversed number (with the appropriate sign) is within `[-0x8000_0000, 0x7fff_ffff]`. If it does not, we return a `0`.

        Args:
            x (int): A signed 32-bit integer whose digits need to be reversed.

        Returns:
            int: The reversed 32-bit integer. If the reversed number is out of range for a 32-bit integer, `0` is returned.

        Time Complexity:
            O(log(x)): As there are approximately `log10(x)` number of digits in x.
        """
        answer = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            answer = x % 10 + answer * 10
            if not (-0x8000_0000 <= (answer * sign) <= 0x7FFF_FFFF):
                return 0
            x //= 10
        return sign * answer
