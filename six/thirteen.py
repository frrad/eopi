from collections import deque


def strings_are_same(str1, str2):
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            return False
    return True


class RollingHasher:
    """Following https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm"""

    def __init__(self, substring_len, base=256, prime_modulus=101):
        self.substring_len = substring_len
        self.base = base
        self.prime_modulus = prime_modulus
        self._char_q = deque()
        self._hash = 0

    def _add_to_hash(self, c):
        self._hash = (self._hash * self.base + ord(c)) % self.prime_modulus
        self._char_q.append(c)

    def _remove_first_in_from_hash(self):
        left_base_offset = 1

        # This for loop should be done once in __init__ and the result saved.
        for i in range(self.substring_len - 1):
            left_base_offset *= self.base
            left_base_offset %= self.prime_modulus
        remove_val = ord(self._char_q.popleft())
        self._hash = self._hash + self.prime_modulus - remove_val * \
            left_base_offset  # adding extra mod val ensures result isn't negative

    def get_hash(self, next_letter):
        if len(self._char_q) == self.substring_len:
            hash_sub = self._remove_first_in_from_hash()
        self._add_to_hash(next_letter)
        return self._hash if len(self._char_q) == self.substring_len else None


def find_substring_start_ind_simple(main_string, substring):
    substring_len = len(substring)
    for start_ind in range(0, len(main_string) - substring_len):
        if strings_are_same(substring, main_string[start_ind:start_ind + substring_len]):
            return start_ind
    return None


def find_substring_start_ind_set(main_string, substring):
    substring_hash = set([substring])
    substring_len = len(substring)
    for start_ind in range(0, len(main_string) - substring_len):
        if main_string[start_ind:start_ind + substring_len] in substring_hash:
            return start_ind
    return None


def find_substring_start_ind_rabin_karp(main_string, substring):
    sub_hasher = RollingHasher(len(substring))
    substring_hash = [sub_hasher.get_hash(c) for c in substring][-1]
    main_hasher = RollingHasher(len(substring))
    for i, c in enumerate(main_string):
        end_ind = i + 1
        start_ind = end_ind - len(substring)
        if substring_hash == main_hasher.get_hash(c) and strings_are_same(substring, main_string[start_ind:end_ind]):
            return start_ind
    return None
