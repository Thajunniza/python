"""
Prime Number Checker (Deterministic, √n Optimization)

This module implements prime number checking using:
    1) Basic trial division
    2) Optimized 6k ± 1 method

Definition:
    A prime number is a natural number greater than 1
    that has exactly two positive divisors: 1 and itself.

Core Methods:
    - is_prime(n): O(√n)        -> Checks divisibility from 2 to √n.
    - is_prime_optimized(n): O(√n) but fewer iterations using 6k ± 1 rule.
"""

class PrimeChecker:
    """Utility class for deterministic prime checking."""

    def is_prime(self, n):
        """
        Check whether n is a prime number using basic trial division.

        Algorithm:
            1) If n <= 1 → not prime.
            2) Check divisibility from 2 to √n.
            3) If any divisor found → return False.
            4) Otherwise → return True.

        Time: O(√n)
        Space: O(1)
        """
        if n <= 1:
            return False

        limit = int(n ** 0.5)
        for i in range(2, limit + 1):
            if n % i == 0:
                return False

        return True

    def is_prime_optimized(self, n):
        """
        Check whether n is prime using 6k ± 1 optimization.

        Key Idea:
            After eliminating multiples of 2 and 3,
            all primes greater than 3 are of the form:

                6k - 1 or 6k + 1

        Algorithm:
            1) Handle small cases (<=3).
            2) Remove multiples of 2 and 3.
            3) Check divisibility for i and i+2 while i <= √n.
               Increment i by 6 each step.

        Time: O(√n) (fewer constant operations)
        Space: O(1)
        """
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        limit = int(n ** 0.5)
        i = 5

        while i <= limit:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6

        return True


# ----------- Example usage / quick sanity run -----------
if __name__ == "__main__":
    checker = PrimeChecker()

    test_cases = {
        -5: False,
        0: False,
        1: False,
        2: True,
        3: True,
        4: False,
        5: True,
        9: False,
        11: True,
        25: False,
        29: True,
        97: True,
        100: False,
        997: True,
        1000: False
    }

    print("Basic Method Results:")
    for num, expected in test_cases.items():
        result = checker.is_prime(num)
        print(f"{num} -> {'PASS' if result == expected else 'FAIL'}")

    print("\nOptimized Method Results:")
    for num, expected in test_cases.items():
        result = checker.is_prime_optimized(num)
        print(f"{num} -> {'PASS' if result == expected else 'FAIL'}")