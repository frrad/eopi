def reverse_words_simple(sentence):
    words = []
    word = ''
    for c in sentence:
        if c == ' ':
            words.append(word)
            words.append(' ')
            word = ''
        else:
            word += c
    words.append(word)

    sentence_rev = ''
    while len(words) > 0:
        sentence_rev += words.pop()

    return sentence_rev


def reverse_words_prealloc(sentence):
    end_ind = len(sentence)
    word = ''
    sentence_rev = [' '] * len(sentence)
    for c in sentence:
        if c == ' ':
            start_ind = end_ind - len(word)
            sentence_rev[start_ind:end_ind] = word
            end_ind = start_ind - 1
            word = ''
        else:
            word += c
    sentence_rev[end_ind - len(word):end_ind] = word

    return ''.join(sentence_rev)
