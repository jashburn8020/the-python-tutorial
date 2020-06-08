"""Demonstrate the `break` and `else` statements on loops."""

from typing import List


def test_for_break_else() -> None:
    """`break` and `else` statements in a `for` loop."""

    def extract_primes(max_num: int) -> List[int]:
        """Extract prime numbers for numbers from 2 to `max_num`."""
        primes: List[int] = []
        for poss_prime in range(2, max_num + 1):
            for poss_factor in range(2, poss_prime):
                if poss_prime % poss_factor == 0:
                    break
            else:
                # loop fell through without finding a factor (without breaking)
                primes.append(poss_prime)
        return primes

    assert extract_primes(2) == [2]
    assert extract_primes(10) == [2, 3, 5, 7]
