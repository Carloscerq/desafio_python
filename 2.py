import math


def is_in_fibonacci(n: int) -> bool:
    """Uses the iterative approach to check if a number is in the Fibonacci sequence.

    Args:
        n (int): The number to check if it is in the Fibonacci sequence

    Returns:
        bool: The result of the check
    """
    if n <= 0:
        return False

    current, next = 0, 1
    while current < n:
        current, next = next, current + next

    return current == n


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"{num} is{"" if is_in_fibonacci(num) else " not" } in the Fibonacci sequence")
