def xor_swap(a, b):
    """Swaps two values without a third variable using XOR swap."""
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


def double_number(n):
    """Doubles a number using left shift (<<)."""
    return n << 1


def detect_different_signs(a, b):
    """Returns True if the numbers have different signs using XOR."""
    return (a ^ b) < 0


def divide_by_two(n):
    """Divides a number by 2 without using the / operator (using right shift)."""
    return n >> 1


# --- Sample Test Execution ---
if __name__ == "__main__":
    x, y = 5, 10
    print("Execution Results:")
    print("-" * 30)

    # 1. Swapping values
    print(f"Before Swap: x = {x}, y = {y}")
    x, y = xor_swap(x, y)
    print(f"After Swap:  x = {x}, y = {y}\n")

    # 2. Doubling and Dividing
    num = 14
    print(f"Original Number: {num}")
    print(f"Doubled (<< 1):  {double_number(num)}")
    print(f"Divided (>> 1):  {divide_by_two(num)}\n")

    # 3. Detecting different signs
    n1, n2, n3 = 4, -7, 12
    print(f"Do {n1} and {n2} have different signs?: {detect_different_signs(n1, n2)}")
    print(f"Do {n1} and {n3} have different signs?: {detect_different_signs(n1, n3)}")
