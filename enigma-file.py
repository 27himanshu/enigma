#!/bin/env python3
"""Crypt text file
usage:
	$ python enigma-file cipher "filename"
	$ python enigma-file decipher "filename" """

import enigma
from sys import argv
(script, todo, filename) = argv
e = enigma.Enigma(
    (0, 0),
    enigma.w_rotor1,
    enigma.w_rotor2,
    enigma.w_reflector,
    enigma.w_plugboard)
key = enigma.Keyboard()
with open(filename, 'r') as plaintxt:
    lines = plaintxt.readlines()
    lines = [line.strip() for line in lines]  # striping newline character
    for l in lines:
        if todo in ("cipher", 'c'):
            print(key.out_text_cipher(e.cipher(key.input_text(l))))
        if todo in ("decipher", 'd'):
            print(key.out_text_decipher(e.cipher(key.input_text(l))))
