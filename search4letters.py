def search4vowels(phrase: str) -> set:
    """Returns the set of vowels found in 'pgrase'."""
    return set('aeiou') & set(phrase)


def search4letters(phrase: str, letters: str = 'aeiou'):
    """Returns the set jf 'letters' found in 'phrase'."""
    return set(letters) & set(phrase)
