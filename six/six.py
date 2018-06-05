def six_nieoh(s):
    l = s.split(' ')
    return ' '.join(reversed(l))

def six_inplace_nieoh(s):
    l = list(s)
    # reverse the list representing the input string
    l.reverse()
    
    # unnecessary space at the end so I don't have to be careful about end conditions
    l.append(' ')  

    # function to reverse a slice from i to j
    def reverse_slice(li, i, j):
        for k in xrange(0, (j-i)//2+1):
            li[i+k], li[j-k] = li[j-k], li[i+k]
    
    # traverse and re-reverse each word
    i = 0
    for j in xrange(0, len(l)):
        if l[j] == ' ':
            reverse_slice(l, i, j-1)
            i = j+1 

    # don't forget to drop that extra space!
    return ''.join(l[:-1])
