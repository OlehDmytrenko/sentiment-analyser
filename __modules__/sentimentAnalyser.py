#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 13:12:17 2022

@author: dmytrenko.o
"""

import sys
stdOutput = open("outlog.log", "w")
sys.stderr = stdOutput
sys.stdout = stdOutput


def emotion(text, model, predictLimit):
    try:
        predict = model.predict(text)
        if (predict[0][0] == '__label__pos') and (predict[1][0] >= predictLimit):
            emotion = "Good"
        elif (predict[0][0] == '__label__neg') and (predict[1][0] >= predictLimit):
            emotion = "Bad" 
        else:
            emotion = None
    except:
        print ("Unexpectable language!")
        emotion = None
    return emotion