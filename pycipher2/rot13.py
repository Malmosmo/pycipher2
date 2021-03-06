# -*- coding: utf-8 -*-
# Author: Hannes Nikulski

from typing import Union
from pycipher2.caesar import Caesar


class Rot13:
    """
    The Rot13 Cipher is a special case of the Caesar Cipher with a key of 13.

    For more information see https://en.wikipedia.org/wiki/ROT13.
    """

    def __init__(self, alphabet: Union[list, str]) -> None:
        self.alphabet = alphabet
        self.cscipher = Caesar(13, self.alphabet)

    def decrypt(self, ciphertext: str) -> str:
        return self.cscipher.decrypt(ciphertext)

    def encrypt(self, plaintext: str) -> str:
        return self.cscipher.encrypt(plaintext)
