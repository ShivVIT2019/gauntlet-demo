def count_vowels(text):
    """Count occurrences of a, e, i, o, and u, regardless of case."""
    return sum(char in "aeiouAEIOU" for char in text)
