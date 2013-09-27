#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@author:Aadesh Neupane
Simple Rules to Map Nepali characters for Speech Processing
"""
"""Follow these guidelines to create the mapper by Wednesday(25th September)"""
#Maps the argumets to the set of rules defined and return the mapped word 

import Tkinter
def map(word):
    a=open("wordlist.txt","r")
    text=a.readlines()
    for line in text:
        #print line
        line=line.strip()
        if len(line)>0:
            for c in line:
                print unicode( c, "utf-8" )


#Contains the set of rules for mapping
def rules():
    dict={"ष":"S AH ","श":"S AH ","स":"S AH ","व":"W AH ","ल":"L AH ","र":"R AH ","य":"Y AH ","म":"M AH ","भ":"BA AH ","ब":"B AH ","फ":"PA AH ","प":"P AH ","न":"N AH ","ध":"DHA AH ","द":"DH AH ","थ":"THA AH ","त":"TH AH ","ण":"N AH ","ढ":"DA AH ","ड":"D AH ","ठ":"TA AH ","ट":"T AH ","ञ":"N AH ","झ":"JHA AH ","ज":"JH AH ","छ":"CHA AH ","च":"CH AH ","ङ":"NG AH ","घ":"GA AH ","ग":"G AH ","ख":"KA AH ","क":"K AH ","औ":"AH UN ","ओ":'OH ',"ऐ":"AH IH ","ए":'EH ',"ऋ":"R IH ","ऊ":'UH ',"उ":'UH ',"ई":'IH ',"इ":'IH ',"आ":'AA ',"अ":'AH ',"ौ":"AH UH","ो":'OH',"ै":"AH IH","े":'EH',"ू":'UH',"ु":'UH',"ी":'IH',"ि":'IH',"ा":'AA',"ं":"M","ँ":"N","ह":"HH AH"}
    print dict["ं"]
    print dict["ष"]

#Main Fuction that takes the file name as the argument and processes the input file to give the results
def main():
    #top=Tkinter.Tk()
    #top.mainloop()
    rules()
    #print dict["ह"]
    #pass

if __name__=='__main__':
    main()
