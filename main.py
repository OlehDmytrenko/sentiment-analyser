#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The program for sentiment analysis of text content.

Input data are a text content, and a language of the text content ("ukr", "rus" and "eng").
By default, the limit of prediction is 0.9.

Output data is "Good" or "Bad" label that describe a emotion of input text content.
In the case of an unexpectable language or a prediction is lower than 0.9, output data is "None".
"""

import sys, os
stdOutput = open("outlog.log", "w")
sys.stderr = stdOutput
sys.stdout = stdOutput

from __modules__ import packagesInstaller
packages = ['os', 'fasttext', 'time']
packagesInstaller.setup_packeges(packages)

from __modules__ import configLoader, modelsLoader, sentimentAnalyser

import time
t0 = time.time()

langModels = configLoader.load_default_languages(os.getcwd())
models = modelsLoader.load_models(os.getcwd(), langModels)

if __name__ == "__main__":
        try:
            text = sys.argv[1]
            lang = sys.argv[2] #format of input languale is "uk", "ru" or "en"
        except:
            print ("¯\_(ツ)_/¯ Error input text data or language!")
            #text = input()
            #lang = input()
    
        sentimentAnalyser.predict_emotion(text, models[lang], configLoader.default_value(os.getcwd(), "predictLimit"))
    
print ("\n ツ You are lucky! The program successfully finished!\n")
print (time.time() - t0)
