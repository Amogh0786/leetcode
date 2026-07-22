class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            for i in range(3, int(x**0.5) + 1, 2):
                if x % i == 0:
                    return False
            return True
        if 8 <= n <= 11:
            return 11
        for length in range(1, 6):
            for root in range(10**(length - 1), 10**length):
                s = str(root)
                p = int(s + s[-2::-1])
                if p >= n and is_prime(p):
                    return p