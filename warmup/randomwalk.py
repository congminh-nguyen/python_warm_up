import random
from typing import Generator, List
import matplotlib.pyplot as plt

def random_walk() -> Generator[int, None, None]:
    """
    Generate steps for a random walk with step size 1.
    
    At each step, moves up (+1) or down (-1) with equal probability.
    The walk continues until reaching a total displacement of 10 units
    from the starting position.
    
    Returns:
        Generator[int, None, None]: A generator yielding the position 
        after each step as an integer.
    """
    position: int = 0
    while abs(position) < 10:
        # Use randint to get -1 or 1 with equal probability
        step: int = 2 * random.randint(0, 1) - 1  # Maps 0->-1, 1->1
        position += step
        yield position

def plot_random_walk() -> None:
    """Plot a random walk."""
    # Collect the steps in a list for plotting
    steps = [0]  # Start at position 0
    for step in random_walk():
        steps.append(step)
        
    plt.figure(figsize=(10, 6))
    plt.plot(steps, marker='o')
    plt.title('Random Walk with Total Displacement of 10')
    plt.xlabel('Step Number')
    plt.ylabel('Position')
    plt.grid(True)
    plt.show()
