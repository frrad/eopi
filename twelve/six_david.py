def find_nearest(s):
    s = s.split()
    d = {}
    min_sep = None
    min_tok = None

    for i, tok in enumerate(s):
        if tok in d:
            sep = i - d[tok]
            if sep < min_sep or min_sep is None:
                min_sep = sep
                min_tok = tok
        d[tok] = i

    return min_tok, min_sep