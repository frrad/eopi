from one_david import Stack

PAREN_MAP = {'}': '{', ')': '(', ']': '['}

def check_parens(s):
    paren_stack = Stack()
    for c in s:
        if c in PAREN_MAP.values():
            paren_stack.push(c)
        elif c in PAREN_MAP.keys():
            opening_paren = paren_stack.pop()
            if PAREN_MAP[c] != opening_paren:
                return False
    if paren_stack.peek() is not None:
        return False
    else:
        return True