# case 1 : input data -> str
def str_bin2dec(bin):
    dec = 0
    for i in range(len(bin)):
        dec += 2**i*int(bin[i])
    return dec

# case 2 : input data -> int
def int_bin2dec(bin):
    dec = 0
    bin = str(bin)
    for i in range(len(bin)):
        dec += 2**i*int(bin[i])
    return dec

def dec2bin(dec):
    bin_list = []
    while True:
        if dec // 2 != 0:
            bin_list.append(dec % 2)
            dec = dec // 2
        else:
            bin_list.append(dec % 2)
            break
    bin_list.reverse()
    bin = ''.join(str(i) for i in bin_list)
    return bin




if __name__ == "__main__":
    ans = str_bin2dec('111')
    print(ans)
    ans = int_bin2dec(111)
    print(ans)
    ans = dec2bin(7)
    print(ans)