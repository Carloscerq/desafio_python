def identify_char_in_string(string: str, char: str) -> int:
    """Identifies the number of times a character appears in a string.

    Args:
        string (str): The string to search
        char (str): The character to search for

    Returns:
        int: The number of times the character appears in the string
    """
    count = 0
    for c in string:
        if c == char:
            count += 1

    return count

if __name__ == "__main__":
    string = input("Enter a string: ")
    char = "a"
    if identify_char_in_string(string, char) == 0:
        print(f"The character '{char}' does not appear in the string")
    else:
        print(f"The character '{char}' appears {identify_char_in_string(string, char)} times in the string")