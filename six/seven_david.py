DIGIT_LETTERS = {
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'Q', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y', 'Z']
}


def get_mnemonics(digits):
    if len(digits) == 1:
        return DIGIT_LETTERS[digits]

    prev_sequences = get_mnemonics(digits[:-1])
    digit = digits[-1]
    letters = DIGIT_LETTERS[digit]

    new_sequences = []
    for seq in prev_sequences:
        for letter in letters:
            new_sequences.append(seq + letter)

    return new_sequences
