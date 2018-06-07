phone_dict = {'1':[''], '2':['A', 'B', 'C'], '3':['D', 'E', 'F'], '4':['G', 'H', 'I'], '5':['J', 'K', 'L'], '6':['M', 'N', 'O'], '7':['P', 'Q', 'R', 'S'], '8':['T', 'U', 'V'], '9':['W', 'X', 'Y', 'Z'], '0':['']}

def nieoh_num_to_char(num):
    if len(num)==1:
        return phone_dict[num[0]]
    ret = []
    num = list(num)
    for char in phone_dict[num[-1]]:
        ret += [n + char for n in nieoh_num_to_char(num[:-1])]
    return ret

