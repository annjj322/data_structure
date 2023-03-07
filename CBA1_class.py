class Bin_compute:
    #class method
    # case 1 : input data -> str
    def str_bin2dec(self, bin):
        self.bin = bin
        dec = 0
        for i in range(len(self.bin)):
            dec += 2**i*int(self.bin[i])
        return dec

    # case 2 : input data -> int
    def int_bin2dec(self, bin):
        self.bin = bin
        dec = 0
        self.bin = str(self.bin)
        for i in range(len(self.bin)):
            dec += 2**i*int(self.bin[i])
        return dec

    def dec2bin(self, dec):
        self.dec = dec
        bin_list = []
        while True:
            if self.dec // 2 != 0:
                bin_list.append(self.dec % 2)
                self.dec = self.dec // 2
            else:
                bin_list.append(self.dec % 2)
                break
        bin_list.reverse()
        bin = ''.join(str(i) for i in bin_list)
        return bin


if __name__ == "__main__":
    a = Bin_compute()
    print(a.dec2bin(21))
    b = Bin_compute()
    print(b.int_bin2dec(10101))
    c = Bin_compute()
    print(c.str_bin2dec('10101'))