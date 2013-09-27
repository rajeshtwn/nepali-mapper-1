#!/usr/bin/env python
# coding: utf8
"""
@author:Aadesh Neupane
Simple Rules to Map Nepali characters for Speech Processing
"""
"""Follow these guidelines to create the mapper by Wednesday(25th September)"""
#Maps the argumets to the set of rules defined and return the mapped word 

import Tkinter
"""def map():
    dict=rules()
    a=open("wordlist.txt","r")
    b=open("out1.txt","w")
    text=a.readlines()
    aa=text[19]
    i=0
    print len(aa)
    b.write(aa+"\t")
    while i <len(aa):
        #print aa[i:i+3]
        chars=aa[i:i+3]
        if chars in dict:
            ab=dict[chars]
            print ab,
            b.write(ab)
        i=i+3
"""
def map():
    dict=rules()
    a=open("word_list.1","r")
    b=open("out1.txt","w")
    text=a.readlines()
    #aa=text[19]
    for aa in text:
        i=0
        print len(aa)
        while i <len(aa):
            #print aa[i:i+3]
            chars=aa[i:i+3]
            if chars in dict:
                ab=dict[chars]
                print ab,
                b.write(ab)
            i=i+3
        b.write("\t"+aa)

#Contains the set of rules for mapping
def rules():
    dict={"ष":"S AH ","श":"S AH ","स":"S AH ","व":"W AH ","ल":"L AH ","र":"R AH ","य":"Y AH ","म":"M AH ","भ":"BA AH ","ब":"B AH ","फ":"PA AH ","प":"P AH ","न":"N AH ","ध":"DHA AH ","द":"DH AH ","थ":"THA AH ","त":"TH AH ","ण":"N AH ","ढ":"DA AH ","ड":"D AH ","ठ":"TA AH ","ट":"T AH ","ञ":"N AH ","झ":"JHA AH ","ज":"JH AH ","छ":"CHA AH ","च":"CH AH ","ङ":"NG AH ","घ":"GA AH ","ग":"G AH ","ख":"KA AH ","क":"K AH ","औ":"AH UN ","ओ":'OH ',"ऐ":"AH IH ","ए":'EH ',"ऋ":"R IH ","ऊ":'UH ',"उ":'UH ',"ई":'IH ',"इ":'IH ',"आ":'AA ',"अ":'AH ',"ौ":"AH UH","ो":'OH',"ै":"AH IH","े":'EH',"ू":'UH',"ु":'UH',"ी":'IH',"ि":'IH',"ा":'AA',"ं":"M","ँ":"N","ह":"HH AH "}
    #print dict["ं"]
    #print dict["ष"]
    return dict

#Main Fuction that takes the file name as the argument and processes the input file to give the results
def main():
    #top=Tkinter.Tk()
    #top.mainloop()
    #rules()
    map()
    #print dict["ह"]
    #pass

if __name__=='__main__':
    main()
