import math
from typing import List, Tuple

def factor_pairs(n: int = 362880) -> List[Tuple[int, int]]:
    """
    Return a list of all pairs of factors of n as tuples.

    This function finds all pairs of factors (i, n // i) such that i * (n // i) = n.
    It iterates from 1 to the square root of n, checking for divisors.

    Parameters:
    n (int): The number for which to find factor pairs. Default is 362880.

    Returns:
    List[Tuple[int, int]]: A list of tuples, where each tuple contains a pair of factors of n.
    """
    return [(i, n // i) for i in range(1, int(n**0.5) + 1) if n % i == 0]

