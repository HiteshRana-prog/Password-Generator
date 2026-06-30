import random
import string


def generate_password(length=12, use_letters=True, use_digits=True, use_symbols=True):
    """Generate a random password based on the given options."""
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=== Python Password Generator ===\n")

    try:
        length = int(input("Enter password length (default 12): ") or 12)
    except ValueError:
        length = 12

    use_letters = input("Include letters? (Y/n): ").strip().lower() != "n"
    use_digits = input("Include numbers? (Y/n): ").strip().lower() != "n"
    use_symbols = input("Include symbols? (Y/n): ").strip().lower() != "n"

    try:
        password = generate_password(length, use_letters, use_digits, use_symbols)
        print(f"\nYour generated password is:\n{password}")
    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
