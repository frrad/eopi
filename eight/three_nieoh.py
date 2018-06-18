def well_formedness(s):
    # Start with a stack
    pancake = []

    for char in s:
        x = Paren(char)
    
        # Append all left parens
        if x.is_left:
            pancake.append(char)

        # Check for each right parens
        elif x.is_right:
            
            # No left parens left in the stack
            if not pancake:
                return False
            
            # Check if the type of right paren is same as last element in pancake
            if x.check_type() != Paren(pancake.pop()).check_type():
                return False

    # Check if any extra left parens are left
    if pancake:
        return False

    return True

class Paren:
    def __init__(self, paren):
        self.paren = paren
        self.left_paren = ['(', '{', '[']
        self.right_paren = [')', '}', ']']
        self.all_paren = self.left_paren + self.right_paren
        self.is_left = paren in self.left_paren
        self.is_right = paren in self.right_paren
        self.is_paren = self.is_left or self.is_right 
        
    def check_type(self):
        if self.paren in ['(', ')']:
            return 'round'
        elif self.paren in ['{', '}']:
            return 'curly'
        elif self.paren in ['[', ']']:
            return 'square'
