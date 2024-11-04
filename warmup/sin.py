import math

# Taylor series expansion for sin(x) up to the 5th order
def taylor_sin(x: float) -> str:
    """
    Calculate the sine of x using the Taylor series expansion up to the 5th order.

    The Taylor series expansion for sin(x) is given by:
    sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...

    This function approximates sin(x) by summing the first three terms of the series:
    term1 = x
    term2 = -x^3 / 3!
    term3 = x^5 / 5!

    Parameters:
    x (float): The input value for which to calculate the sine.

    Returns:
    a descriptive string stating the order expanded to and value to 5 decimal places
    """
    # Terms of the Taylor series for sin(x)
    term1 = x
    term2 = -x**3 / math.factorial(3)
    term3 = x**5 / math.factorial(5)
    
    # Sum of the terms
    approx_sin = term1 + term2 + term3
    
    return f"Taylor series approximation of sin({x}) to 5th order: {approx_sin:.5f}"

