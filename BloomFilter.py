class BloomFilter:

    def __init__(self, f_len = 32):
        self.filter_len = f_len
        self.filter_arr =  0


    def hash1(self, str1):
        resultat = 32
        for c in str1:
            code = ord(c)
            resultat = (resultat * 17 + code) % self.filter_len
        return resultat


    def hash2(self, str1):
        resultat = 0
        for c in str1:
            code = ord(c)
            resultat = (resultat * 223 + code) % self.filter_len
        return resultat


    def add(self, str1):
        if isinstance(str1, str):
            self.filter_arr |= 1 << self.hash1(str1)
            self.filter_arr |= 1 << self.hash2(str1)

    def is_value(self, str1):
        if isinstance(str1, str):
            if self.filter_arr & 1 << self.hash1(str1) == 0: return False
            if self.filter_arr & 1 << self.hash2(str1) == 0: return False
            return True