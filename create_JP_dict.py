#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 13:18:23 2022

@author: john
"""
import pandas as pd
file = open('JMdict_e', 'r')
lines = file.readlines()
file.close()

kanji = None
pronounciation = None

dict_ = {}

nbr = 0
for l in lines:

    
    if "<keb>" in l and kanji is None:
        
        tmp = l[5:]
        i_end = tmp.find("<")
        kanji = tmp[:i_end]

    if kanji is not None:
        
        if "<reb>" in l and pronounciation is None:
            
            tmp = l[5:]
            i_end = tmp.find("<")
            pronounciation= tmp[:i_end]
            
            english = ""
            
        if pronounciation is not None:
           

        
            if "<gloss>" in l:

                if english != "":
                    
                    english += ", "                

                tmp = l[7:]
                i_end = tmp.find("<")
                english +=  tmp[:i_end] 


                        

                
            if english is not None and "</sense>" in l:

                dict_details = {}
                dict_details["kanji"] = kanji                  
                dict_details["pron"] = pronounciation
                dict_details["en"] = english
                
                dict_[nbr] = dict_details
     
                kanji = None
                pronounciation = None
                
                nbr += 1

        
df = pd.DataFrame.from_dict(dict_).transpose()
df.to_csv ('jmdict.csv', index = False, header=True)