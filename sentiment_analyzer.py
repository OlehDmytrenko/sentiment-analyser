# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 12:30:47 2021

@author: Олег Дмитренко

The program for sentiment analysis of text content.

Input data are a text content, and a language of the text content ("ukr", "rus" and "eng").
By default, the limit of prediction is 0.9.

Output data is "Good" or "Bad" label that describe a emotion of input text content.
In the case of an unexpectable language or a prediction is lower than 0.9, output data is "None".
"""

import os
import fasttext

def sentiment_analyser(text, lang, predictLimit):
    if lang != None:
        if lang == "ukr":
            predict = modelUkr.predict(text)
            if (predict[0][0] == '__label__pos') and (predict[1][0] >= predictLimit):
                emotion = "Good"
            elif (predict[0][0] == '__label__neg') and (predict[1][0] >= predictLimit):
                emotion = "Bad" 
            else:
                emotion = None
        elif lang == "rus":
            predict = modelRus.predict(text)
            if (predict[0][0] == '__label__pos') and (predict[1][0] >= predictLimit):
                emotion = "Good"
            elif (predict[0][0] == '__label__neg') and (predict[1][0] >= predictLimit):
                emotion = "Bad" 
            else:
                emotion = None
        elif lang == "eng":
            predict = modelEng.predict(text)
            if (predict[0][0] == '__label__pos') and (predict[1][0] >= predictLimit):
                emotion = "Good"
            elif (predict[0][0] == '__label__neg') and (predict[1][0] >= predictLimit):
                emotion = "Bad"  
            else:
                emotion = None
        else:
            print ("Unexpectable language!")
            emotion = None
    return emotion

def load_models():
    modelUkr = fasttext.load_model(os.path.join('Models', 'ukr_infostream_v2.ftz'))
    modelRus = fasttext.load_model(os.path.join('Models', 'rus_infostream.ftz'))
    modelEng = fasttext.load_model(os.path.join('Models', 'eng_infostream_v2.ftz'))
    print ("Models successfully loaded!\n")
    return modelUkr, modelRus, modelEng

if __name__ == "__main__":
    modelUkr, modelRus, modelEng = load_models() 
    
    text = input()
    lang = input() #format of input languale is "ukr", "rus" or "eng"
    predictLimit = 0.9
    emotion = sentiment_analyser(text, lang, predictLimit)
    print (emotion)
    