# -*- coding: utf-8 -*-
"""
Enigma
Created on Tue Apr  7 20:52:00 2015

@author: himanshu
"""
import sys
class Rotor():
    def __init__(self, s=[17, 6, 13, 21, 2, 16, 3, 10, 20, 14, 5, 12, 1, 4,
                              0, 19, 22, 11, 23, 18, 7, 9, 25, 15, 8, 24],n = 0,
                              r=False):
        self.settings=s
        self.notch=n
        self.number_spin=0
        self.is_reflector=r
        return
    def spin(self):
        self.number_spin=self.number_spin+1
        if(self.number_spin>26):
            self.number_spin=0
        self.notch=self.notch+1
        if(self.notch>25):
            self.notch=0
        return
    def map_forward(self,i):
        index=self.settings.index(i)
        if(index<25):
            return self.settings[index+1]
        else:
            return self.settings[0]
    def map_backward(self,i):
        index=self.settings.index(i)
        if(index>0):
            return self.settings[index-1]
        else:
            return self.settings[25]
    def map_reflect(self,i):
        index=self.settings.index(i)
        if(index % 2!= 0):
            return self.settings[index-1]
        else:
            return self.settings[index+1]
        
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
    def input_text(self,text='This is Enigma'):
        text=text.replace(' ',"xz")
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
        return o_text

class Enigma():
    def __init__(self):
        self.r1=Rotor()
        self.r2=Rotor()
        self.r3=Rotor(r=True)
        return
    def cipher(self,in_text):
        out_text=[]
        for i in in_text:
            j=self.r1.map_forward(i)
            self.r1.spin()
            if(self.r1.number_spin==26):
                self.r2.spin()
            j=self.r2.map_forward(j)
            if(self.r2.number_spin==26):
                self.r3.spin()
            j=self.r3.map_reflect(j)
            j=self.r2.map_backward(j)
            j=self.r1.map_backward(j)
            out_text.append(j)
        return out_text
    def decipher(self,in_text):
        out_text=[]
        for i in in_text:
            j=self.r1.map_forward(i)
            self.r1.spin()
            if(self.r1.number_spin==26):
                self.r2.spin()
            j=self.r2.map_forward(j)
            if(self.r2.number_spin==26):
                self.r3.spin()
            j=self.r3.map_reflect(j)
            j=self.r2.map_backward(j)
            j=self.r1.map_backward(j)
            out_text.append(j)
        return out_text
        

if __name__== "__main__":
    arg=sys.argv
    arg2=arg[2:]
    arg2=''.join(arg2)
    eng=Enigma()
    key=Keyboard()
    if(arg[1]=="cipher" or arg[1]=="c"):
        print("Ciphered text is: "+ key.out_text_cipher(eng.cipher(key.input_text(arg2))))
    if(arg[1]=="decipher" or arg[1]=="d"):
        print("Decphered text is: " + key.out_text_decipher(eng.decipher(key.input_text(arg2))))
