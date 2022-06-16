print('Imported model')

text = 'Variable consisting of string of chars'

def find_element(target, sequence):
    """Find an element in a sequence"""
    for index, value in enumerate(sequence):
        if value == target:
            return index
        return -1

def find_longest_word(sequence):
    """Finds the longest element in a sequence"""
    longest_word = ''
    for word in sequence:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word