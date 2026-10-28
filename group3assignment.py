# ============================================================
# Computer Architecture - Group 3
# Course Code: 25AIM34
# Question 1: Signed Binary Arithmetic using 8-bit 2's Complement
# Question 2: Rotate Right Operations (ROR and RCR)
# ============================================================

# -------------------- QUESTION 1 -----------------------------

def to_8bit_binary(number):
    """Convert a signed integer to 8-bit 2's complement."""
    return format(number & 0xFF, '08b')


def signed_value(binary):
    """Convert an 8-bit binary string to a signed integer."""
    value = int(binary, 2)
    if value >= 128:
        value -= 256
    return value


def binary_arithmetic(a, b, operation):
    """Perform 8-bit signed binary arithmetic."""
    binary_a = to_8bit_binary(a)
    binary_b = to_8bit_binary(b)

    if operation == '+':
        result = a + b
        binary_result = format(
            (int(binary_a, 2) + int(binary_b, 2)) & 0xFF, '08b'
        )
        overflow = (a >= 0 and b >= 0 and result > 127) or (
            a < 0 and b < 0 and result < -128
        )

    elif operation == '-':
        result = a - b
        binary_result = format(
            (int(binary_a, 2) - int(binary_b, 2)) & 0xFF, '08b'
        )
        overflow = (a >= 0 and b < 0 and result > 127) or (
            a < 0 and b >= 0 and result < -128
        )

    else:
        raise ValueError("Invalid operation")

    print(f"Operand A: {a:4d} = {binary_a}")
    print(f"Operand B: {b:4d} = {binary_b}")
    print(f"Operation: {operation}")
    print(f"Binary result: {binary_result}")

    if overflow:
        print(f"Signed decimal result: {result} (overflow)")
        print(f"8-bit signed interpretation: {signed_value(binary_result)}")
        print("Arithmetic overflow: YES")
    else:
        print(f"Decimal result: {result}")
        print("Arithmetic overflow: NO")

    print("-" * 50)


print("=" * 50)
print("QUESTION 1: SIGNED BINARY ARITHMETIC")
print("=" * 50)

print("\n(a) +48 + (+23)")
binary_arithmetic(48, 23, '+')

print("\n(b) (-46) - (-29)")
binary_arithmetic(-46, -29, '-')


# -------------------- QUESTION 2 -----------------------------

def rotate_right(binary, positions):
    """Rotate an 8-bit binary string right without carry."""
    value = int(binary, 2)
    positions %= 8
    return format(
        ((value >> positions) | (value << (8 - positions))) & 0xFF,
        '08b'
    )


def rotate_right_carry(binary, carry, positions):
    """Rotate right through carry using a 9-bit register."""
    value = int(binary, 2)
    register = (carry << 8) | value

    for step in range(1, positions + 1):
        print(f"Step {step}:")
        print(f"  Before: Carry={register >> 8}, "
              f"Binary={register & 0xFF:08b}")

        # Rotate the 9-bit register right by one position.
        register = ((register >> 1) | ((register & 1) << 8)) & 0x1FF

        print(f"  After:  Carry={register >> 8}, "
              f"Binary={register & 0xFF:08b}")

    return format(register & 0xFF, '08b'), (register >> 8) & 1


print("\n" + "=" * 50)
print("QUESTION 2: ROTATE OPERATIONS")
print("=" * 50)

original = "11010101"
positions = 2

# (a) Rotate Right Without Carry (ROR)
print("\n(a) ROTATE RIGHT WITHOUT CARRY (ROR)")
print(f"Original binary: {original}")

current = original
for step in range(1, positions + 1):
    current = rotate_right(current, 1)
    print(f"After step {step}: {current}")

print(f"Final ROR result: {current}")


# (b) Rotate Right Through Carry (RCR)
print("\n(b) ROTATE RIGHT WITH CARRY (RCR)")
print(f"Original binary: {original}")

initial_carry = 0
print(f"Initial carry flag: {initial_carry}")

final_binary, final_carry = rotate_right_carry(
    original, initial_carry, positions
)

print(f"Final RCR binary result: {final_binary}")
print(f"Final carry flag: {final_carry}")

print("\n" + "=" * 50)
print("PROGRAM EXECUTION COMPLETED")
print("=" * 50)
