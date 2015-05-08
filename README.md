# Enigma


Implimentation of Enigma machine using python language.

This implimentation consists of two rotors, one reflector and one plugboard.

More rotors can be added and their wiring can also be changed if required. Default plugboard has ten wires.

Plain text (unciphered text) can contain all 26 alphabets, spaces, full-stops, quetion-marks, '@', '-', '(', ')' and '#' (but no other characters are allowed)

Default wirings for the two rotors, one reflector and plugboard are:

 | ABCDEFGHIJKLMNOPQRSTUVWXYZ 
  --- | --- 
rotor no. 1 | DMTWSILRUYQNKFEJCAZBPGXOHV 
rotor no. 2 | HQZGPJTMOBLNCIFDYAWVEUSRKX 
reflector | EJMZALYXVBWFCRQUONTSPIKHGD 
plugboard | BADCFEHGJILKNMPORQTSUVWXYZ 

The wirings are such that in rotor no. 1 : A maps to D, B maps to M and so forth.


Usage
```shell
$ python enigma.py cipher hello world
>>Ciphered text is: xfdwhamqadtn
$ python enigma.py decipher xfdwhamqadtn
>>Deciphered text is: hello world
$ python enigma-file.py cipher "plaint-text-filename.txt"
$ python enigma-file.py decipher "encrypted-text-filename.txt"
```
