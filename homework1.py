def countdown_and_up(n):
    """Count down from n to 1, then back up."""
    if n > 0:
        print(*range(n, 0, -1))
        print(*range(2, n + 1))

# Example usage
countdown_and_up(5)


