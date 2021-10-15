def print_upper_words(words):
    """For a list of words, print out each word on a separate line, but in all uppercase. """
    for word in words:
        print(word.upper())

def print_Eore_words(words):
    """only prints words that start with the letter ‘e’ (either upper or lowercase)."""
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word)

def print_upper_words_must(words, startLetter):
    """only prints words that start with startLetter, uppercased"""
    for word in words:
      for letter in startLetter:
        if word.startswith(letter):
            print(word.upper())

print_upper_words_must(["ello", "Ey", "goodbye", "yo", "yes"], "y")