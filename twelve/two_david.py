from collections import defaultdict

def is_constructible(letter, magazine):
    letter_counter = defaultdict(int)
    remaining_chars = len(letter)
    
    for letter_char in letter:
        letter_counter[letter_char] += 1
        
    for mag_char in magazine:
        if letter_counter.get(mag_char, 0) > 0:
            letter_counter[mag_char] -= 1
            remaining_chars -= 1
            if remaining_chars == 0:
                break
            
    return remaining_chars == 0