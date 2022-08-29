#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 14:25:49 2022

@author: john
"""

import pandas as pd

all_hiragana = [""]

kyu = 7
str_ = str(kyu) + "級"

dict_name = str_ + "_dict.csv"
kanken_kanjis = pd.read_csv("kanken_kanji.csv")
columns = kanken_kanjis.columns
index = columns.get_loc(str_)

kyu_kanji_list = list(kanken_kanjis.iloc[:, index].dropna())

all_kanji_list = []
for i in range(index+1) :
    
    kanji_list = list(kanken_kanjis.iloc[:, i].dropna())    
    all_kanji_list += kanji_list
    
    
jmdict = pd.read_csv("jmdict.csv")
kanji_series = jmdict["kanji"]
all_words_list = list(kanji_series)

hiragana = pd.read_csv("hiragana.csv",header=None)



all_hiragana_list = list(hiragana.iloc[:, 0])

all_valid_characters = all_hiragana_list + all_kanji_list

dict_ = {}

nbr = 0
for k in kyu_kanji_list :
    
    for w in all_words_list:
        
    
        if k in w:
            
            for c in w:
                
                if c in all_valid_characters:
                    OK = True
                else: 
                    OK = False
                    break
            if OK:
                # print(k,w)
                
                ind = pd.Index(all_words_list).get_loc(w)
                pronounciation = jmdict.iloc[ind, 1]
                english = jmdict.iloc[ind, 2]

                
                if type(pronounciation) != pd.core.series.Series:
                    dict_[nbr] = {"word": w ,"pron": pronounciation, "en": english }                
                    nbr += 1


df = pd.DataFrame.from_dict(dict_).transpose()
df.to_csv (dict_name, index = False, header=True)