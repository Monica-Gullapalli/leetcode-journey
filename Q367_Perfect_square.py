class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = math.sqrt(num)
        return x.is_integer()
        