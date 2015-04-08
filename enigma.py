# -*- coding: utf-8 -*-
"""
Enigma
Created on Tue Apr  7 20:52:00 2015
@author: himanshu
"""

w_rotor1=[3, 12, 19, 22, 18, 8, 11, 17, 20, 24, 16, 13, 10, 5, 4, 9, 2, 0,
          25, 1, 15, 6, 23, 14, 7, 21]
w_rotor2=[7, 16, 25, 6, 15, 9, 19, 12, 14, 1, 11, 13, 2, 8, 5, 3, 24, 0,
          22, 21, 4, 20, 18, 17, 10, 23]
w_reflector=[16, 24, 7, 14, 6, 13, 4, 2, 21, 15, 20, 25, 19, 5, 3, 9, 0, 23,
             22, 12, 10, 8, 18, 17, 1, 11]
""" w_rotor1 , w_rotor2 and w_reflector are default mappings/wiring of each rotor:


                    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    w_rotor1:       DMTWSILRUYQNKFEJCAZBPGXOHV
    w_rotor2:       HQZGPJTMOBLNCIFDYAWVEUSRKX
    w_reflector:    EJMZALYXVBWFCRQUONTSPIKHGD
    
    Mappings are such tha in rotor1 A maps to D, B maps to M and so forth."""    

class Rotor():
    """Create new rotors with wirings
    """

                              
    def __init__(self, wiring, is_reflector=False, offset=0):
        """ wiring: a list containing mapping of rotor
            is_reflector: True if the rotor act as a reflector (by default set to False)
            offset: current offset of rotor
            number_spin: store the number of times rotor is rotated"""
        self.wiring=wiring
        self.offset=offset
        self.number_spin=0
        self.is_reflector=is_reflector
        for _ in range(offset):
            self.spin()
        return
    def spin(self):
        """call this function to spin/step forward the rotor """
        self.number_spin=self.number_spin+1
        if(self.number_spin>26):
            self.number_spin=0
        self.offset=self.offset+1
        if(self.offset>25):
            self.offset=0
        self.wiring=self.wiring[25:]+self.wiring[:25]
        return
    def map_forward(self,i):
        """map element forward (right to left)"""
        return self.wiring[i]
    def map_backward(self,i):
        """map element backward (left to right)"""
        index=self.wiring.index(i)
        return index
    def map_reflect(self,i):
        """map element in reflector"""
        return self.wiring[i]
        
        
class Plugboard():
    def __init__(self,size=10,s=[(0,1),(2,3),(4,5),(6,7),(8,9),(10,11),
                                     (12,13),(14,15),(16,17),(18,19)]):
        try:
            size!=len(s)
        except:
            print("Number of plugboard cables does not match the current\
            settings")
        self.size=size
        self.settings=s
        
        
class Keyboard():
    """Create a keyboard.
        This keyboard maps alphabets to integer.
        Also maps a space with "xz"
        a fullstop with "wq"
        and a question mark with "ds"."""
    def input_text(self,text='This is Enigma'):
        text=text.replace(' ',"xz")
        text=text.replace('.', "wq")
        text=text.replace('?',"ds")
        in_text=[]
        text=text.lower()
        for i in text:
            in_text.append(ord(i)%97)
        return in_text
    def out_text_cipher(self,text=[0,1,2,3]):
        o_text=[]
        for i in text:
            o_text.append(chr(i+97))
        o_text=''.join(o_text)
        return o_text
    def out_text_decipher(self,text=[0,1,2,3]):
        o_text=[]
        for i in text:
            o_text.append(chr(i+97))
        o_text=''.join(o_text)
        o_text=o_text.replace("xz"," ")
        o_text=o_text.replace("wq",".")
        o_text=o_text.replace("ds","?")
        return o_text

class Enigma():
    """Takes four arguments of which last three are wiring settings for 2 rotors and a reflector
    First argument is a tuple of two elements containing offset of two rotors"""       
    def __init__(self,off, wiring1, wiring2, wiring3):
        self.wiring1=wiring1
        self.wiring2=wiring2
        self.wiring3=wiring3
        self.off=off        
        self.r1=Rotor(self.wiring1,offset=off[0])
        self.r2=Rotor(self.wiring2,offset=off[1])
        self.r3=Rotor(self.wiring3, is_reflector=True)
        
    def reset(self):
        """Resets the current instance to its initial settings"""
        self.r1(self.wiring1,offset=self.off[0])
        self.r2(self.wiring3,offset=self.off[1])
        self.r3(self.wiring3, is_reflector=True)
        return
    def cipher(self,in_text):
        """Encode the list in_text and return the encoded list"""
        out_text=[]
        for i in in_text:
            j=self.r1.map_forward(i)
            j=self.r2.map_forward(j)
            j=self.r3.map_reflect(j)
            j=self.r2.map_backward(j)
            j=self.r1.map_backward(j)
            out_text.append(j)
            self.r1.spin()
            if(self.r1.number_spin==26):
                self.r2.spin()
        return out_text

if __name__== "__main__":
    import sys
    arg=sys.argv
    string=arg[2:]
    string=' '.join(string)
    enigma=Enigma((0,0), w_rotor1, w_rotor2, w_reflector)
    key=Keyboard()
    if(arg[1]=="cipher" or arg[1]=="c"):
        print("Ciphered text is: "+ key.out_text_cipher(enigma.cipher(key.input_text(string))))
    if(arg[1]=="decipher" or arg[1]=="d"):
        print("Decphered text is: " + key.out_text_decipher(enigma.cipher(key.input_text(string))))
