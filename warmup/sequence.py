import math
from typing import List

def sieve_of_eratosthenes(n: int) -> List[int]:
    """
    Return a list of prime numbers less than n using the Sieve of Eratosthenes algorithm.

    The Sieve of Eratosthenes is an ancient algorithm used to find all prime numbers up to a specified integer.
    It works by iteratively marking the multiples of each prime number starting from 2.

    Parameters:
    n (int): The upper limit (exclusive) for the range of numbers to check for primality.

    Returns:
    List[int]: A list of prime numbers less than n.
    """
    if n <= 2:
        return []

    # Initialize a list to track prime status of numbers
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Implement the Sieve of Eratosthenes
    for start in range(2, int(n**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start*start, n, start):
                is_prime[multiple] = False

    # Extract the list of primes
    return [num for num, prime in enumerate(is_prime) if prime]

def recaman_sequence(n: int) -> List[int]:
    """
    Return a list of the first n terms in the Recaman's sequence.

    Recaman's sequence is a well-known sequence in mathematics, defined as follows:
    a(0) = 0
    for n > 0:
        a(n) = a(n-1) - n if the result is positive and not already in the sequence,
               otherwise a(n) = a(n-1) + n

    Parameters:
    n (int): The number of terms to generate in the sequence.

    Returns:
    List[int]: A list containing the first n terms of the Recaman's sequence.
    """
    if n <= 0:
        return []

    sequence = [0] * n
    seen = set()
    seen.add(0)

    for i in range(1, n):
        current = sequence[i - 1] - i
        if current > 0 and current not in seen:
            sequence[i] = current
        else:
            sequence[i] = sequence[i - 1] + i
        seen.add(sequence[i])

    return sequence

def common_elements_in_lists(n: int) -> List[int]:
    """
    Return a list of numbers that appear in both the prime list and Recaman's sequence.

    This function generates a list of prime numbers less than n using the Sieve of Eratosthenes algorithm
    and the first n terms of Recaman's sequence. It then finds the intersection of both lists.

    Parameters:
    n (int): The upper limit for the prime numbers and the number of terms in Recaman's sequence.

    Returns:
    List[int]: A list of numbers that appear in both the prime list and Recaman's sequence.
    """
    primes = sieve_of_eratosthenes(n)
    recaman = recaman_sequence(n)
    
    # Find the intersection of both lists
    common_elements = list(set(primes) & set(recaman))
    
    return common_elements


