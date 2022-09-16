#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 16:39:26 2022

@author: john
"""

import pandas as pd

frequencies_df = pd.read_csv("BCCWJ_frequencylist_luw2_ver1_0.tsv", sep='\t')
all_words_series = frequencies_df["lemma"]
all_words_frequencies = frequencies_df["pmw"]

# ind = all_words_series[all_words_series == "不幸"]
ind = pd.Index(all_words_series).get_loc("不幸")
max_freq = max(all_words_frequencies.iloc[ind]/10000)

kyu = 7
str_ = str(kyu) + "級"
dict_name = str_ + "_dict.csv"

word_df = pd.read_csv(dict_name)

word_list = list(word_df["word"])


hiragana = pd.read_csv("hiragana.csv",header=None)
all_hiragana_list = list(hiragana.iloc[:, 0])

basic_compounds = []
long_word_list = []

for w in word_list:

    for h in all_hiragana_list:
        
        if h in w:
            
            break

    if len(w) == 2:
        basic_compounds.append(w)
    
        
        for w2 in word_list :
            
            if len(w2) > 2:
                
                if w in w2:
                    
                    long_word_list.append(w2)
                    
dict_freq = {}
dict_missing = []
nbr = 0
for w in basic_compounds:
    
    try:
        ind = pd.Index(all_words_series).get_loc(w)
    except:
        dict_missing.append(w)
        ind = None

    if ind is not None :

        freq = all_words_frequencies.iloc[ind]/10000
        if type(freq) == pd.core.series.Series:
            freq = max(freq)
        
        dict_freq[nbr] = {"word": w, "freq" : freq}
        nbr += 1

freq_dict_name = str_ + "_dict_high_freq.csv"
df = pd.DataFrame.from_dict(dict_freq).transpose()
df.to_csv (freq_dict_name, index = False, header=True)