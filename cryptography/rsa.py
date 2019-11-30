
import sympy
from logzero import logger

P = 7
Q = 13


class RSA:
    def __init__(self, p, q):
        self.__p = p
        self.__q = q
        self.__n = self.__p * self.__q
        self.__fi = (self.__p - 1) * (self.__q - 1)

        for e in range(2, self.__fi):
            if self.gcd(e, self.__fi) == 1:
                self.__e = e
                break
        else:
            raise RuntimeError("Can't find a right e")

        for i in range(1, 10):
            x = 1 + i * self.__fi
            if x % self.__e == 0:
                self.__d = int(x / self.__e)
                break
        else:
            raise RuntimeError("Can't find a right d")

    @property
    def p(self):
        return self.__p

    @p.setter
    def p(self, p):
        if sympy.isprime(p):
            self.__p = p
        raise RuntimeError("p should be prime")

    @property
    def q(self):
        return self.__q

    @q.setter
    def q(self, q):
        if sympy.isprime(q):
            self.__q = q
        raise RuntimeError("p should be prime")

    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        return RSA.gcd(b, a % b)

    def encrypt(self, plain_text):
        return plain_text ** self.__e % self.__n

    def decrypt(self, encrypted_text):
        return encrypted_text ** self.__d % self.__n

    def __str__(self):
        result = ''
        result += 'p: {}\n'.format(self.__p)
        result += 'q: {}\n'.format(self.__q)
        result += 'n: {}\n'.format(self.__n)
        result += 'fi: {}\n'.format(self.__fi)
        result += 'e: {}\n'.format(self.__e)
        result += 'd: {}'.format(self.__d)
        return result


if __name__ == "__main__":
    rsa = RSA(P, Q)
    print(rsa)
    while True:
        plain_text = int(input('Enter plain text: '))
        cipher_text = rsa.encrypt(plain_text)
        decrypted_text = rsa.decrypt(cipher_text)

        logger.info("Plain text: {}".format(plain_text))
        logger.info("Cipher text: {}".format(cipher_text))
        logger.info("Decrypted text: {}".format(decrypted_text))
